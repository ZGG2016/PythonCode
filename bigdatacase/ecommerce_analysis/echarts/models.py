from django.db import models

# Create your models here.

class viewafter(models.Model):
    count=models.IntegerField(u'计数')
    itemid=models.IntegerField(u'商品',primary_key=True)
    property=models.CharField(u'属性',max_length=50)

    def __str__(self):
        return self.property

    class Meta:
        db_table = "viewafter"

class cartafter(models.Model):
    count=models.IntegerField(u'计数')
    itemid=models.IntegerField(u'商品',primary_key=True)
    property=models.CharField(u'属性',max_length=50)

    def __str__(self):
        return self.property

    class Meta:
        db_table = "cartafter"

class transafter(models.Model):
    count=models.IntegerField(u'计数')
    itemid=models.IntegerField(u'商品',primary_key=True)
    property=models.CharField(u'属性',max_length=50)

    def __str__(self):
        return self.property

    class Meta:
        db_table = "transafter"