from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView
from .models import Message
from .models import Lastnews
from .models import IpModel
from .models import Hire
from django.core.cache import cache
from django.db import connection
from home.models import Category
from home.models import Web
from home.models import ChatBOT
from home.models import DataAnalysis
from home.models import PersonalCV

# Create your views here.

def home(request):
    newsdata=Lastnews.objects.all();
    web1=Web.objects.all();
    chat = ChatBOT.objects.all();
    analysis =DataAnalysis.objects.all();

    data={
        'newsdata':newsdata,
        'web1':web1,
        'chat':chat,
        'analysis':analysis,
    }
    return render(request, 'index.html',data)


def message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Email =request.POST.get('Email')
        Comment=request.POST.get('Comment')
        

        mess=Message(
            name=name,
            Email =Email,
            Comment =Comment,
            
        )
        mess.save()
        redirect('index.html')
    return render(request, 'index.html')

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for is not None:
        ip=x_forwarded_for.split(',')[0]
    else:
        ip= request.META.get('REMOTE_ADDR')
    return ip

def lastnews(request,pk):
    title = request.POST.get('title')
    news_desc = request.POST.get('news_desc')
    news_image = request.POST.get('news_image')
    

    last =Lastnews(
        title=title,
        news_desc=news_desc,
        news_image=news_image,
    )
    
    return redirect('/')

def postlike(request, pk):
    post_id = request.POST.get("blog_id")
    post = Lastnews.objects.get(pk = post_id)
    ip = get_client_ip(request)


    if not IpModel.objects.filter(ip=ip).exists():
        IpModel.objects.create(ip=ip)
    if post.likes.filter(id=IpModel.objects.get(ip=ip).id).exists():
        post.likes.remove(IpModel.objects.get(ip=ip))
    else:
        post.likes.add(IpModel.objects.get(ip=ip)) 
    return HttpResponseRedirect(reverse('lastnews', args=[post_id]))

def HireMe(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email =request.POST.get('email')
        whatsapp=request.POST.get('whatsapp')
        Requirement=request.POST.get('Requirement')

        hire=Hire(
            name=name,
            email =email,
            whatsapp =whatsapp,
            Requirement=Requirement
        )
        hire.save()
    return render(request, 'hireme.html')