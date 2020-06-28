
from pyspark.ml.feature import MinMaxScaler
from pyspark.mllib.evaluation import RegressionMetrics
from pyspark.mllib.regression import LabeledPoint,LinearRegressionWithSGD
from pyspark.sql import SparkSession

# 线性回归模型预测

def get_lp(s):
    return LabeledPoint(s['label'],s['scaled'].toArray())

def f(s):
    ss = s.split(",")
    return LabeledPoint(ss[0][1:],[ss[1],ss[2][:-1]])

path_in_train="file:///E:/Code/python_spark/cases/chicago_taxi/data/train_data/part-00000"
path_in_test="file:///E:/Code/python_spark/cases/chicago_taxi/data/test_data/part-00000"
result="file:///E:/Code/python_spark/cases/chicago_taxi/output/rlt"

spark = SparkSession \
        .builder \
        .appName("min_max_scaler") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()

rdd = spark.sparkContext.textFile(path_in_test)
test_data=rdd.map(lambda x:f(x))  # 测试数据

train_data = spark.read.format("libsvm").load(path_in_train)
scaler = MinMaxScaler(inputCol="features", outputCol="scaled")
scalerModel = scaler.fit(train_data)
df = scalerModel.transform(train_data)
#df.show()
data = df.rdd.map(lambda s:get_lp(s))  #归一化后的训练数据

# 训练模型
model = LinearRegressionWithSGD.train(data, iterations=100,step=0.01)
valuesAndPreds = test_data.map(lambda p: (p.label, model.predict(p.features)))
#print(valuesAndPreds.collect())
metrics = RegressionMetrics(valuesAndPreds)
# Squared Error
print("MSE = %s" % metrics.meanSquaredError)

