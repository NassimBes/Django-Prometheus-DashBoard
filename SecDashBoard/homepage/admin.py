from django.contrib import admin
from .models import PromServerModel,ServerInfoModel
# Register your models here.


admin.site.register(PromServerModel)
admin.site.register(ServerInfoModel)