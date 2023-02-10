from django.urls import path

from . import views
urlpatterns = [
    path('', views.home , name='home'),
    path('Comment',views.message, name='Comment'),
    path('lastnews/<slug:pk>',views.lastnews, name='lastnews'),
    path('Like/<slug:pk>', views.postlike, name='blog_like'),
    path('Hire',views.HireMe, name='HireMe'),
]
