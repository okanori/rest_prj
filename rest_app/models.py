from django.db import models


# Create your models here.
class Position(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(verbose_name='名前', max_length=20)
    latitude = models.DecimalField(verbose_name='緯度', max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField(verbose_name='経度', max_digits=9, decimal_places=6, default=0)
    update = models.DateTimeField(verbose_name='更新日')
