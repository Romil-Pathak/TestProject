from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    
    path('',views.index),
    path('usersignup/',views.usersignup),
    path('home/',views.home,name='home'),
    path('userlogout/',views.userlogout),
    #path('loginuser/',views.loginuser,name='loginuser'),
    path('newuser/',views.newuser,name='newuser'),
    #path('showdata/',views.showdata,name='showdata'),
    path('deletedata/<int:stid>',views.deletedata),
    path('updatedata/<int:stid>',views.updatedata),

]
