from django.db import models

from homepage.models import PromServerModel

# Create your models here.
class TargetModel(models.Model):
    targets = models.ForeignKey(PromServerModel,on_delete=models.DO_NOTHING)
    status = models.BooleanField()
    scrape_duration = models.CharField(max_length=60,null=True,blank=True)
    metrics = models.JSONField(default=list)
    


    