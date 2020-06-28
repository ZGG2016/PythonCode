import redis
from django.shortcuts import render,HttpResponse

from BookStore import settings

pool = redis.ConnectionPool(host=settings.redis_host,port=6379)

def shares_show(request):

    r=redis.StrictRedis(connection_pool=pool)
    keys = r.keys()
    date=[]
    day_amt=[]
    month_amt=[]
    newDate=[]
    for key in keys:
        value = str(r.get(key),encoding='utf-8')
        date.append(str(key, encoding='utf-8'))
        day_amt.append(float(value.split("-")[0]))
        month_amt.append(float(value.split("-")[1]))
    dict=mysort(date)
    for i in dict:
        for j in dict[i]:
            tmpstr=i+" "+j
            newDate.append(tmpstr)
    return render(request,'echarts.html',locals())

def mysort(date):

    list1=[] ; list2=[] ; list3=[] ; list4=[]
    list5=[] ;list6=[] ; list7=[] ; list8=[]
    list9=[] ; list10=[] ; list11=[] ; list12=[]

    dict={}
    for i in date:
            mon = i.split(" ")[0]
            day = i.split(" ")[1]
            if mon=="Jan":
                list1.append(day)
            elif mon=="Feb":
                list2.append(day)
            elif mon=="Mar":
                list3.append(day)
            elif mon=="Apr":
                list4.append(day)
            elif mon=="May":
                list5.append(day)
            elif mon=="Jun":
                list6.append(day)
            elif mon=="Jul":
                list7.append(day)
            elif mon=="Aug":
                list8.append(day)
            elif mon=="Sep":
                list9.append(day)
            elif mon=="Oct":
                list10.append(day)
            elif mon=="Nov":
                list11.append(day)
            elif mon=="Dec":
                list12.append(day)
    dict["Jan"] = list1
    dict["Feb"] = list2
    dict["Mar"] = list3
    dict["Apr"] = list4
    dict["May"] = list5
    dict["Jun"] = list6
    dict["Jul"] = list7
    dict["Aug"] = list8
    dict["Sep"] = list9
    dict["Oct"] = list10
    dict["Nov"] = list11
    dict["Dec"] = list12
    list1.sort()
    list2.sort()
    list3.sort()
    list4.sort()
    list5.sort()
    list6.sort()
    list7.sort()
    list8.sort()
    list9.sort()
    list10.sort()
    list11.sort()
    list12.sort()

    return dict