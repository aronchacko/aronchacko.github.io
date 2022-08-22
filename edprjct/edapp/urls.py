from unicodedata import name
from django import views
from . import views
from django.urls import path,include
from edapp import views


urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('loginpage2',views.loginpage2,name='loginpage2'),
    path('registerpage',views.registerpage,name='registerpage'),
    path('classrompage',views.classroompage,name='classroompage'),
    path('librapage',views.librapage,name='librapage'),
    path('cbsepage',views.cbsepage,name='cbsepage'),
    path('icsepage',views.icsepage,name='icsepage'),
    
    path('usercreate',views.usercreate,name="usercreate"),
    path('user_login',views.user_login,name="user_login"),
    path('logout',views.logout,name="logout")
    
    
   
]
