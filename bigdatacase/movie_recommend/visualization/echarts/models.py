from django.db import models

# Create your models here.

class recommend(models.Model):

    id=models.IntegerField(u'用户', primary_key=True)
    moviename=models.CharField(u'电影',max_length=30)
    pref=models.FloatField(u'评分')

    def __str__(self):
        return self.moviename

    class Meta:
        db_table = "recommend"