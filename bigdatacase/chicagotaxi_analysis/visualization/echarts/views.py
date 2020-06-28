from django.shortcuts import render
from .models import taxi
# Create your views here.

def shares_show(request):
    shares_result=taxi.objects.all()
    lat_lon = []
    for item in shares_result:
        list = item.latandlon.split('::')
        lat_lon.append([float(list[1]),float(list[0])])  #注意经纬度的顺序，先经后纬

    return render(request, 'echarts.html', locals())



