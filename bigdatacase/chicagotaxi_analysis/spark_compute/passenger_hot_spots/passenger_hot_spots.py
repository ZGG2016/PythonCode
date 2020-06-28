from operator import add

import os
from pyspark import SparkContext


def filter_data(s):
    ss = s.split(",")
    if "Trip ID" not in s and len(ss)==23 and ss[17]!="" and ss[18]!="":
        return s

def get_data(s):
    ss = s.split(",")
    return (ss[17]+","+ss[18],1)

path_in="data/taxi_test.csv"
path_out="phs/"

sc = SparkContext("local")
rdd = sc.textFile(path_in)

rlt=rdd.filter(lambda x:filter_data(x)).map(lambda x:get_data(x))\
    .reduceByKey(add).filter(lambda x:x[1]>=2)

rlt.saveAsTextFile(path_out)

#将数据导入mysql,需要先建表
# os.system("sqoop export --connect jdbc:mysql://(IP地址):3306/userdb?useUnicode=true "
#           "--username root --table result --export-dir /phs/part-r-00000 "
#           "--driver com.mysql.jdbc.Driver --input-fields-terminated-by '\t'")