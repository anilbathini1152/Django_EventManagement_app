from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('usrsignup',views.usignup, name='usignup'),
    path('login',views.ulogin,name='ulogin'),
    path('logout',views.ulogout,name='ulogout'),
    path('uprof',views.uprof,name='uprof'),
    path('usrprofupdate',views.usrprofupdate,name='usrprofupdate'),
    path('evntregiser/',views.evntregister,name='evntregister'),
    path('myregistrations/',views.myregistrations,name='myregistrations'),
    path('contactus',views.contactus,name='contactus')
    #path(r'^evntregiser/(?P<evntid>.*)$',views.evntregister,name='evntregister'),
]
