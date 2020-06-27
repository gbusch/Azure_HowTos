# simple example script.
# run with `python test.py`

def get_spark():
    from pyspark.sql import SparkSession
    spark = SparkSession.builder.getOrCreate()
    
    return spark


if __name__ == "__main__":
    spark = get_spark()
    print(spark.range(100).count())
