from django.db import models

# Create your models here.

#类名要和表名一致  字段和表中字段一致
class taxi(models.Model):
    latandlon = models.CharField(u'经纬度',primary_key=True,max_length=200)
    count = models.CharField(u'计数', max_length=200)

    class Meta:
        db_table = "taxi"