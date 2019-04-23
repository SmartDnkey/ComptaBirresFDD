from django.db import models
from datetime import datetime


class Edicio(models.Model):

    class Meta(object):
        verbose_name = "edicio"
        verbose_name_plural = "edicions"

    edicio = models.IntegerField(unique=True)
    totalBirres = models.IntegerField(default=0)

    def __str__(self):
        return "%s" % (self.edicio)

    def sumaBirra(self):

        self.totalBirres = self.totalBirres + 1
        self.save()



class Tirador(models.Model):

    class Meta(object):
        verbose_name = "tirador"
        verbose_name_plural = "tiradors"

    name = models.CharField(max_length=50, null=True)
    totalBirresTirador = models.IntegerField(default=0)
    ip = models.GenericIPAddressField(protocol='IPv4', default="0.0.0.0", null=True)

    def __str__(self):
        return "%s" % (self.name)

    def addBirra(self):
        self.totalBirresTirador = self.totalBirresTirador + 1


class Birra(models.Model):

    class Meta(object):
        verbose_name = "birra"
        verbose_name_plural = "birres"

    timestamp = models.DateTimeField(default=datetime.now())
    edicio = models.ForeignKey(Edicio, on_delete=models.CASCADE)
    tirador = models.ForeignKey(Tirador, on_delete=models.CASCADE)





