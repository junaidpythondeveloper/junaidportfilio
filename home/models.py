from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
from datetime import datetime,date

# Create your models here.
class IpModel(models.Model):
    ip = models.CharField( max_length=100)

    def __str__(self):
        return self.ip
    

class Message(models.Model):
    name =models.CharField( max_length=50)
    Email = models.EmailField( max_length=254)
    Comment = models.CharField(max_length=1000)

class Category(models.Model):
    name=models.CharField (max_length=150)

class Lastnews(models.Model):
    title=models.CharField( max_length=50)
    authors = models.ForeignKey(User, on_delete=models.CASCADE)
    news_desc=HTMLField()
    news_image= models.FileField( upload_to="news/",max_length=250, null=True,default=None)
    news_image1= models.FileField( upload_to="news/",max_length=250, null=True,default=None)
    news_image2= models.FileField( upload_to="news/",max_length=250, null=True,default=None)
    video= models.FileField( upload_to="news/",max_length=250, null=True,default=None)
    likes = models.ManyToManyField(IpModel, related_name="post_likes", blank=True)
    category=models.CharField(max_length=150, default="coding")
    post_data = models.DateField( auto_now_add=True)

    def __str__(self):
        return self.title
    

    def total_likes(self):
        return self.likes.count()

class Hire(models.Model):
    name=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    whatsapp=models.CharField( max_length=70)
    Requirement=HTMLField()

class Web(models.Model):
    img1=models.FileField( upload_to="news/",  max_length=250, null=True,default=None)
    img2=models.FileField( upload_to="news/",  max_length=250,null=True,default=None)
    img3=models.FileField( upload_to="news/",  max_length=250,null=True,default=None)
    img4=models.FileField( upload_to="news/",  max_length=250,null=True,default=None)
    img4=models.FileField( upload_to="news/",  max_length=250,null=True,default=None)
    img4=models.FileField( upload_to="news/",  max_length=250,null=True,default=None)
    img5=models.FileField( upload_to="news/",  max_length=250,null=True,default=None)
    img6=models.FileField( upload_to="news/",   max_length=250,null=True,default=None)
    img7=models.FileField( upload_to="news/",  max_length=250,null=True,default=None)
    img8=models.FileField( upload_to="news/",  max_length=250,null=True,default=None)

class ChatBOT(models.Model):
    img1=models.FileField( upload_to="news/",  max_length=250, null=True,default=None)
    img2=models.FileField( upload_to="news/",  max_length=250,null=True,default=None)
    img3=models.FileField( upload_to="news/",  max_length=250,null=True,default=None)
    img4=models.FileField( upload_to="news/",  max_length=250,null=True,default=None)

class DataAnalysis(models.Model):
    img1=models.FileField( upload_to="news1/",  max_length=250, null=True,default=None)
    img2=models.FileField( upload_to="news1/",  max_length=250,null=True,default=None)
    img3=models.FileField( upload_to="news1/",  max_length=250,null=True,default=None)
    img4=models.FileField( upload_to="news1/",  max_length=250,null=True,default=None)

class PersonalCV(models.Model):
    cv= models.FileField(upload_to="news1/",  max_length=250, null=True,default=None)