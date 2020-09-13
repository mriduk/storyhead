
from . import views

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import home,story_details,count_reader,logout


urlpatterns = [
    #path('',views.home,name='home'),
    #path('', views.home,name='home'),
    path('', home.as_view(), name='home'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    url('sign_up/',views.sign_up, name='sign_up'),
   path('<slug:pk>/', story_details.as_view(), name='story_details'),
    path('<slug:story_id>/count_reader/',views.count_reader,name='count_reader'),
    
    
    
]

# app_name='first_auth'
# urlpatterns = [
#     #path('',views.home,name='home'),
#     #path('', views.home,name='home'),
    
#    path('',views.sign_up, name='sign_up'),
#   path('login/', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
#   path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
#    path('<slug:pk>/', story_details.as_view(), name='story_details'),
#     path('<slug:story_id>/count_reader/',views.count_reader,name='count_reader'),
    
    
    
    
# ]



