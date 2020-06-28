from django.shortcuts import render
from .models import result
# Create your views here.

def shares_show(request):
    shares_result = result.objects.all()
    return render(request, 'echarts.html', locals())