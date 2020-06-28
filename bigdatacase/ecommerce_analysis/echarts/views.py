from django.shortcuts import render
from .models  import viewafter
from .models  import cartafter
from .models  import transafter
# Create your views here.

def shares_show(request):
    shares_view = viewafter.objects.all()
    shares_cart = cartafter.objects.all()
    shares_trans = transafter.objects.all()
    return render(request, 'echarts.html', locals())