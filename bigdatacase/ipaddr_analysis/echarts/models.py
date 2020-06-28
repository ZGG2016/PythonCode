from django.db import models

# Create your models here.

class ip(models.Model):
    ipaddr = models.CharField(u'ip地址',max_length=100, null=True)
    longitude = models.FloatField(u'经度', null=True)
    latitude = models.FloatField(u'纬度', null=True)
    city = models.CharField(u'城市',max_length=100, null=True)

    class Meta:
        db_table = "ip"