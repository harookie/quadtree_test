from pyspark import SparkContext


def test_spark():
    sc = SparkContext(master="local", appName="first app")
    df = sc.parallelize(range(0, 10))
    print(df.collect())
    sc.stop()
