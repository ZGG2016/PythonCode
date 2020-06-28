from django.db import models

# Create your models here.


class result(models.Model):
    id=models.IntegerField(u'编号',primary_key=True)
    name = models.CharField(u'名字', max_length=200)
    latitude = models.FloatField(u'纬度')
    longitude = models.FloatField(u'经度')
    mysum = models.IntegerField(u'总和')
    price = models.CharField(u'价格', max_length=100)

    def __str__(self):
        return self.name,self.price

    class Meta:
        db_table = "result"