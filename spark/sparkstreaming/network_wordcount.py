import sys
from operator import add

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

"""
To run this on your local machine, you need to first run a Netcat server
    `$ nc -lk 9999`
 and then run the example
    `$ bin/spark-submit examples/src/main/python/streaming/network_wordcount.py localhost 9999`
"""

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: network_wordcount.py <hostname> <port>", file=sys.stderr)
        sys.exit(-1)

    sc = SparkContext(appName="PythonStreamingNetworkWordCount")
    ssc = StreamingContext(sc,1)

    lines = ssc.socketTextStream(sys.argv[1], int(sys.argv[2]))

    counts = lines.flatMap(lambda x:x.split(" "))\
        .map(lambda x:(x,1))\
        .reduceByKey(add)

    counts.pprint()

    ssc.start()
    ssc.awaitTermination()