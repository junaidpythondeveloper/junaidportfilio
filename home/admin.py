from django.contrib import admin
from home.models import Message
from home.models import Lastnews
from home.models import IpModel
from home.models import Category
from home.models import Web
from home.models import ChatBOT
from home.models import DataAnalysis
from home.models import PersonalCV

class messageadmin(admin.ModelAdmin):
    list_display=('name','Email','Comment')

admin.site.register(Message,messageadmin)

class lastadmin(admin.ModelAdmin):
    
    list_display=('title','authors','news_desc','news_image','news_image1','news_image2','category','post_data')

admin.site.register(Lastnews,lastadmin)

class ipmodeladmin(admin.ModelAdmin):
    list_display =('ip',)
admin.site.register(IpModel,ipmodeladmin)

admin.site.register(Category)

admin.site.register(Web)
admin.site.register(ChatBOT)
admin.site.register(DataAnalysis)
admin.site.register(PersonalCV)
# Register your models here.
