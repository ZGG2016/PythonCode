from django.db import models

# Create your models here.

class result(models.Model):
    date = models.CharField(u'日期',max_length=100,null=True)
    day_amt = models.CharField(u'日销售额',max_length=100000000,null=True)
    month_amt = models.CharField(u'月销售额',max_length=100000000,null=True)

class Meta:
    db_table = "result"