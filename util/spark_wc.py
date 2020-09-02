import sys
from operator import add
from pyspark import SparkContext, SparkConf

# spark wordcount

def main(flag):
    global data
    conf = SparkConf().setMaster("spark://zgg:7077").setAppName("wordcount")
    sc = SparkContext(conf=conf)

    # data = sc.parallelize(["a,b","b,c"])

    # 从hdfs读取文件  hdfs://localhost:9000/user/hadoop/word.txt
    if flag=='0':
        data = sc.textFile("hdfs://zgg:9000/in/wc.txt")
        #data = sc.textFile("/in/wc.txt")

    # 从本地读取文件 --- 绝对路径
    elif flag=='1':
        data = sc.textFile("file:///root/data/wc.txt")

    rdd = data.flatMap(lambda x:x.split(" ")).map(lambda x:(x,1)).reduceByKey(add)

    rlt = rdd.collect()
    for (word,count) in rlt:
        print(word,count)

    sc.stop()

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("input params,please")

    """"
     0：从hdfs读
     1：从本地读
    """

    flag = sys.argv[1]
    main(flag)

"""
集群运行：
spark-submit spark_wc.py 
    --master yarn-cluster \
    --queue mid \
    --num-executors $NUM_EXECUTORS \
    --driver-memory $DRIVER_MEMORY \
    --executor-memory $EXECUTOR_MEMORY \
    --executor-cores $EXECUTOR_CORES \

---------------------------------------------

系统默认是从hdfs://localhost:9000/目录下读取文件的，但是README.md文件在本地目录下，
并不在这一目录下，所以sc.textFile()必须使用绝对路径。
"""




