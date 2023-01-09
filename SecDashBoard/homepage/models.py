from django.db import models

# Create your models here.



class PromServerModel(models.Model):
    hostname = models.CharField(max_length=50,null=True,blank=True)
    ipAddress = models.GenericIPAddressField()
    activeTargets = models.JSONField(default=list)
    droppedTargets = models.JSONField(default=list)

    def __str__(self):
        return self.hostname
    

class ServerInfoModel(models.Model):
    pass
    # hostname = models.OneToOneField(
    #     ServerModel,
    #     on_delete=models.DO_NOTHING,
    #     primary_key=False
    #     )
    # state =  models.BooleanField()
    # scrape_duration = models.CharField(max_length=50,null=True,blank=True)


    # def __str__(self) -> str:
    #     return f"{self.hostname} INFO MODEL"



    # class Meta:
    #     ordering = ['state']


