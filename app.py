from pyspark.sql import SparkSession


def main():
    # Initialize SparkSession
    spark = SparkSession.builder \
        .appName("HelloWorld") \
        .master("spark://localhost:7077") \
        .getOrCreate()

    # Create an RDD containing numbers from 1 to 1000
    numbers_rdd = spark.sparkContext.parallelize(range(1, 1000))

    # Sum the elements in the RDD
    total = numbers_rdd.sum()

    print(f"Sum of numbers from 1 to 1000 is: {total}")

    # Stop the SparkSession
    spark.stop()


if __name__ == "__main__":
    main()