from pyspark.sql import SparkSession
from pyspark.sql.functions import size, split, avg, rank, col
from pyspark.sql.window import Window

# Create Spark session
spark = SparkSession.builder \
    .appName("GamingProfiles2025_Steam") \
    .getOrCreate()

steam_base = "C:/gaming_profiles/steam/"

steam_files = {
    "achievements": steam_base + "achievements.csv",
    "friends": steam_base + "friends.csv",
    "games": steam_base + "games.csv",
    "history": steam_base + "history.csv",
    "players": steam_base + "players.csv",
    "prices": steam_base + "prices.csv",
    "private_ids": steam_base + "private_steamids.csv",
    "purchased": steam_base + "purchased_games.csv",
    "reviews": steam_base + "reviews.csv"
}

steam_dfs = {
    name: spark.read.csv(path, header=True, inferSchema=True)
    for name, path in steam_files.items()
}

# === Null Handling ===
if steam_dfs["players"] is not None:
    steam_dfs["players"] = steam_dfs["players"].na.drop(subset=["country"])

if steam_dfs["purchased"] is not None:
    steam_dfs["purchased"] = steam_dfs["purchased"].filter(
        col("library").isNotNull() & (col("library") != "")
    )

if steam_dfs["prices"] is not None:
    steam_dfs["prices"] = steam_dfs["prices"].filter(col("usd").isNotNull())

if steam_dfs["history"] is not None:
    steam_dfs["history"] = steam_dfs["history"].na.drop(subset=["date_acquired"])

if steam_dfs["achievements"] is not None:
    steam_dfs["achievements"] = steam_dfs["achievements"].fillna({
        "title": "Unknown Title",
        "description": "No Description"
    })

# === Show Schemas and Samples ===
for name, df in steam_dfs.items():
    print(f"\n===== {name.upper()} =====")
    df.printSchema()
    df.show(5)

# b. Create New Column: Number of Games
steam_library = steam_dfs['purchased'].withColumn(
    "num_games", size(split("library", ","))
)

# a. Filtering (5 Queries)
steam_dfs['games'].filter("release_date > '2023-01-01'").show()
steam_dfs['players'].filter("country = 'Brazil'").show()
steam_dfs['reviews'].filter("helpful > 0").show()
steam_dfs['prices'].filter("usd > 50").show()
steam_dfs['players'].filter("country = 'Brazil' OR country = 'United Kingdom'").show()

# c. Aggregate Functions
steam_library.agg({"num_games": "avg"}).show()
steam_library.agg({"num_games": "max"}).show()

# d. Grouping: Number of players per country
steam_dfs['players'].groupBy("country").count().orderBy("count", ascending=False).show(5)

# e. Sorting: Top players by number of games
steam_library.orderBy("num_games", ascending=False).show(5)

# f. Join: Players with their number of games
joined_steam = steam_dfs['players'].join(steam_library, "playerid")
joined_steam.select("playerid", "country", "num_games").show(5)

# g. Window Function: Rank players by num_games
windowSpec = Window.orderBy(steam_library["num_games"].desc())
steam_library.withColumn("rank", rank().over(windowSpec)) \
    .select("playerid", "num_games", "rank").show(5)

# h. Aggregate Window Function: Average num_games by country
country_window = Window.partitionBy("country")
joined_steam.withColumn("country_avg", avg("num_games").over(country_window)) \
    .select("playerid", "country", "num_games", "country_avg").show(5)
