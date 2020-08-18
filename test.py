
import sys,xlrd
from operator import add

from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext


from time import ctime, sleep

import time, functools

from pyhive import hive

