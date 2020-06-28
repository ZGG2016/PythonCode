from pyspark import SparkContext
from pyspark.mllib.regression import LabeledPoint

#分别获取训练数据、测试数据
from pyspark.mllib.util import MLUtils


def filter_data(s):
    ss = s.split(",")
    if "Trip ID" not in s and len(ss) == 23 and ss[4]!='0' and ss[5]!='0' and ss[14]!='0' :
        return s

def get_test_data(s):  # 4:time 5:mile 14:pay
    sss = s.split(",")
    return float(sss[14][1:]),float(sss[4])/60.0,float(sss[5])

def get_train_data(s):  # 4:time 5:mile 14:pay
    sss = s.split(",")
    return LabeledPoint(float(sss[14][1:]),[float(sss[4])/60.0,float(sss[5])])

path_in="file:///E:/Code/python_spark/cases/chicago_taxi/data/taxi_test.csv"
path_out_test="file:///E:/Code/python_spark/cases/chicago_taxi/data/test_data"
path_out_train="file:///E:/Code/python_spark/cases/chicago_taxi/data/train_data"

sc = SparkContext("local")
rdd = sc.textFile(path_in)

#抽样出测试数据并过滤特征
data_test = rdd.sample(False,0.3).filter(lambda line:filter_data(line))\
   .map(lambda line:get_test_data(line))
#获取训练数据并转成需要的格式
data_train = rdd.filter(lambda line:filter_data(line))\
   .map(lambda line:get_train_data(line))
#data_train.saveAsTextFile(path_out_train)
data_test.saveAsTextFile(path_out_test)
MLUtils.saveAsLibSVMFile(data_train,path_out_train)