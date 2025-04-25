from pyspark.sql import SparkSession
from pyspark.sql.functions import size, split, avg, rank, col
from pyspark.sql.window import Window

# Start the Spark session
spark = SparkSession.builder \
    .appName("GamingProfiles2025_Xbox") \
    .getOrCreate()

xbox_base = "C:/gaming_profiles/xbox/"
xbox_files = {
    "achievements": xbox_base + "achievements.csv",
    "games": xbox_base + "games.csv",
    "history": xbox_base + "history.csv",
    "players": xbox_base + "players.csv",
    "prices": xbox_base + "prices.csv",
    "purchased": xbox_base + "purchased_games.csv"
}

# Load and fill missing values
xbox_dfs = {name: spark.read.csv(path, header=True, inferSchema=True) for name, path in xbox_files.items()}

# Handle nulls - removed 'platform' which doesn't exist in Xbox dataset
xbox_dfs['games'] = xbox_dfs['games'].fillna({
    "genres": "Unknown",
    "developers": "Unknown",
    "publishers": "Unknown"
})

xbox_dfs['prices'] = xbox_dfs['prices'].fillna({
    "usd": 0.0, "eur": 0.0, "gbp": 0.0, "jpy": 0.0, "rub": 0.0
})

xbox_dfs['players'] = xbox_dfs['players'].fillna({"nickname": "Unknown"})

xbox_dfs['purchased'] = xbox_dfs['purchased'].na.drop(subset=["playerid", "library"])

# Show schemas and previews
for name, df in xbox_dfs.items():
    print(f"\n===== XBOX - {name.upper()} =====")
    df.printSchema()
    df.show(3)

# b. Create New Column: Number of Games
xbox_library = xbox_dfs['purchased'].withColumn(
    "num_games", size(split("library", ","))
)

# a. Filtering (5 Queries)
xbox_dfs['games'].filter("release_date > '2023-01-01'").show()
xbox_dfs['players'].filter("nickname = 'smrnov'").show()
xbox_dfs['prices'].filter("usd > 50").show()
xbox_dfs['games'].filter("genres LIKE '%Action%'").show()
xbox_dfs['players'].filter("playerid > 1000000").show()

# c. Aggregate Functions
xbox_library.agg({"num_games": "avg"}).show()
xbox_library.agg({"num_games": "max"}).show()

# d. Grouping: PlayerID buckets
xbox_dfs['players'].withColumn("id_group", xbox_dfs['players']["playerid"] % 3) \
    .groupBy("id_group").count().show()

# e. Sorting: Top players by number of games
xbox_library.orderBy("num_games", ascending=False).show(5)

# f. Join: Players with their number of games
joined_xbox = xbox_dfs['players'].join(xbox_library, "playerid")
joined_xbox.select("playerid", "nickname", "num_games").show(5)

# g. Window Function: Rank players by num_games
xbox_library = xbox_library.withColumn("id_group", xbox_library["playerid"] % 3)
windowSpec = Window.partitionBy("id_group").orderBy(col("num_games").desc())

xbox_library.withColumn("rank", rank().over(windowSpec)).select(
    "playerid", "id_group", "num_games", "rank"
).show(5)

# h. Aggregate Window Function: Avg num_games by group
windowSpecGroup = Window.partitionBy("id_group")
joined_xbox.withColumn("id_group", joined_xbox["playerid"] % 3) \
    .withColumn("group_avg", avg("num_games").over(windowSpecGroup)) \
    .select("playerid", "num_games", "group_avg").show(5)
