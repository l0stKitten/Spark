from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.sql.functions import col

# Create a SparkSession
spark = SparkSession.builder \
    .appName("FIlmRecommendation") \
    .getOrCreate()

# Load the user-song listening history data
film_history = spark.read.csv("MovieUserRating.csv", header=True, inferSchema=True,  sep = ',')

# Prepare the data for training
film_history = listening_history.select("userId", "movieId", "rating")

# Split the data into training and testing sets
(training_data, testing_data) = film_history.randomSplit([0.8, 0.2])

# Build the recommendation model using ALS
als = ALS(userCol="userId", movieCol="movieId", ratingCol="rating", coldStartStrategy="drop")
model = als.fit(training_data)

# Generate top 10 recommendations for each user in the testing set
recommendations = model.recommendForAllUsers(10)

# Show the recommendations for a specific user
user_id = 1
user_recommendations = recommendations.filter(recommendations.user_id == user_id).select("recommendations")
user_recommendations.show(truncate=False)

id_to_retrieve = 1

filtered_data = indexed_data.filter(col("movieIndex") == id_to_retrieve)

movie_index = filtered_data.select("movie").collect()[0][0]
print(movie_index)

df_original = spark.read.format("csv").options(**csv_options).load(data_path)

artist_name = (df_original.filter(col("movieId") == movie_index)).select("title").collect()[0][0]
print(artist_name)

genre_name = (df_original.filter(col("movieId") == movie_index)).select("genres").collect()[0][0]
print(genre_name)
