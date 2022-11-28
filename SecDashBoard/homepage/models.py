from django.db import models

# Create your models here.



class ServerModel(models.Model):
    hostname = models.CharField(max_length=50,null=True,blank=True)
    ipAddress = models.GenericIPAddressField()


class ServerInfoModel:
    pass