from django.shortcuts import render
from .models  import recommend
# Create your views here.

def shares_show(request):
    #从数据库读取数据
    shares = recommend.objects.all()
    return render(request, 'echarts.html', locals())
