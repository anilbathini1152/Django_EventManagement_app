from django.urls import path
from . import views

urlpatterns = [
    path('home',views.orghome,name='orghome'),
    path('addevents',views.addevents,name='addevents'),
    path('myevents',views.viewevnts,name='myevents'),
    path('orgprof',views.orgprof,name='orgprof'),
    path('cpasswd',views.changepasswd,name='changepasswd')
    
   
]
