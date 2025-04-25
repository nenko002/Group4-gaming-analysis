ps_base = "C:/gaming_profiles/playstation/"


ps_files = {
    "achievements": ps_base + "achievements.csv",
    "games": ps_base + "games.csv",
    "history": ps_base + "history.csv",
    "players": ps_base + "players.csv",
    "prices": ps_base + "prices.csv",
    "purchased": ps_base + "purchased_games.csv"
}


from pyspark.sql import SparkSession

# Start the Spark session
spark = SparkSession.builder \
    .appName("GamingProfiles2025_PlayStation") \
    .getOrCreate()

ps_dfs = {name: spark.read.csv(path, header=True, inferSchema=True) for name, path in ps_files.items()}


# Fill missing values
ps_dfs['players'] = ps_dfs['players'].fillna({'country': 'Unknown'})
ps_dfs['games'] = ps_dfs['games'].fillna({
    'developers': 'Unknown',
    'publishers': 'Unknown',
    'genres': 'Unknown',
    'supported_languages': 'Unknown'
})
ps_dfs['prices'] = ps_dfs['prices'].fillna({'usd': 0.0})

# Drop rows with null playerid or gameid in critical joins (optional)
for key in ['purchased', 'history']:
    if key in ps_dfs:
        ps_dfs[key] = ps_dfs[key].dropna(subset=['playerid'])

for name, df in ps_dfs.items():
    print(f"\n===== PLAYSTATION - {name.upper()} =====")
    df.printSchema()
    df.show(3)

from pyspark.sql.functions import size, split, avg, rank
from pyspark.sql.window import Window

# b. Create New Column: Number of Games
ps_library = ps_dfs['purchased'].withColumn(
    "num_games", size(split("library", ","))
)

# a. Filtering (5 Queries)
ps_dfs['games'].filter("release_date > '2023-01-01'").show()
ps_dfs['players'].filter("country = 'Brazil'").show()
ps_dfs['games'].filter("platform = 'PS5'").show()
ps_dfs['prices'].filter("usd > 50").show()
ps_dfs['players'].filter("country = 'Brazil' OR country = 'United Kingdom'").show()

# c. Aggregate Functions
ps_library.agg({"num_games": "avg"}).show()
ps_library.agg({"num_games": "max"}).show()

# d. Grouping: Number of players per country
ps_dfs['players'].groupBy("country").count().orderBy("count", ascending=False).show(5)

# e. Sorting: Top players by number of games
ps_library.orderBy("num_games", ascending=False).show(5)

# f. Join: Players with their number of games
joined_ps = ps_dfs['players'].join(ps_library, "playerid")
joined_ps.select("playerid", "country", "num_games").show(5)

# g. Window Function: Rank players by num_games
windowSpec = Window.orderBy(ps_library["num_games"].desc())
ps_library.withColumn("rank", rank().over(windowSpec)) \
    .select("playerid", "num_games", "rank").show(5)

# h. Aggregate Window Function: Average num_games by country
country_window = Window.partitionBy("country")
joined_ps.withColumn("country_avg", avg("num_games").over(country_window)) \
    .select("playerid", "country", "num_games", "country_avg").show(5)

