from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.ml.feature import StringIndexer
from pyspark.sql.functions import col

# Create a Spark session
spark = SparkSession.builder.appName("Film Recommender").getOrCreate()

# Set the options for reading the CSV file
csv_options = {
    "header": "true",
    "encoding": "utf-8",
    "sep": ","
}

# Load the MovieLens dataset
data_path = "MovieUserRating.csv"
df = spark.read.csv("MovieUserRating.csv", header=True, inferSchema=True,  sep = ',')

# Select relevant columns and rename them
df = df.select("userId", "movieId", "rating").withColumnRenamed("userId", "user").withColumnRenamed("movieId", "movie")

# Convert rating column to float
df = df.withColumn("rating", df["rating"].cast("float"))

# Filter out any invalid or missing values
df = df.filter(df["user"].isNotNull() & df["rating"].isNotNull() & df["movie"].isNotNull())


# Split the data into training and testing sets (80% for training, 20% for testing)
train_data, test_data = df.randomSplit([0.8, 0.2], seed=42)

# Create StringIndexers for the user and song columns
user_indexer = StringIndexer(inputCol="user", outputCol="userIndex")
movie_indexer = StringIndexer(inputCol="movie", outputCol="movieIndex")

# Fit StringIndexers and transform the data
indexed_data = user_indexer.fit(train_data).transform(train_data)
indexed_data = movie_indexer.fit(indexed_data).transform(indexed_data)

# Create an ALS recommender model
als = ALS(userCol="userIndex", itemCol="movieIndex", ratingCol="rating", nonnegative=True)

# Fit the model to the training data
model = als.fit(indexed_data)

user_indexer = StringIndexer(inputCol="user", outputCol="userIndex")
movie_indexer = StringIndexer(inputCol="movie", outputCol="movieIndex")

# Fit StringIndexers and transform the data
indexed_test_data = user_indexer.fit(test_data).transform(test_data)
indexed_test_data = movie_indexer.fit(indexed_test_data).transform(indexed_test_data)

id_to_retrieve = 1

filtered_data = indexed_data.filter(col("movieIndex") == id_to_retrieve)

movie_index = filtered_data.select("movie").collect()[0][0]

print(movie_index)

df_original = spark.read.format("csv").options(**csv_options).load(data_path)

film_name = (df_original.filter(col("movieId") == movie_index)).select("title").collect()[0][0]

print(film_name)
