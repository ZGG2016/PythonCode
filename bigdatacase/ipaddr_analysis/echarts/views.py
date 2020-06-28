from django.shortcuts import render, HttpResponse
import redis
from Ipaddr import settings
# Create your views here.

pool=redis.ConnectionPool(host=settings.redis_host,port=6379)

def shares_show(request):

    list = get_info()
    mydata = []
    mydata2 = {}
    for item in list:
        mydata.append({'name':item['4'],'value':item['1']})
    for item in list:
        mydata2[item['4']]=[item['2'],item['3']]
    return render(request, 'echarts.html', locals())

 #从数据库读取数据
def get_info():
    r = redis.StrictRedis(connection_pool=pool)
    keys = r.keys()
    list = []
    for key in keys:
        value=str(r.get(key), encoding='utf-8')
        longitude = value.split(",", 2)[0]
        latitude = value.split(",", 2)[1]
        city = value.split(",", 2)[2]
        ipaddr=str(key,encoding='utf-8')
        dict={'1':ipaddr,'2':longitude,'3':latitude,'4':city}
        list.append(dict)
    return list