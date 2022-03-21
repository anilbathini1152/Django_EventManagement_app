from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import Events,Evntorganisers
from home.models import IsOrganiser
from django.contrib.auth import authenticate, login, logout
from datetime import date
import datetime
from home.views import usignup,ulogin,home

# Create your views here.
#home page for organiser
def orghome(request):
    if request.user.is_authenticated:
        sts=IsOrganiser.objects.get(username=request.user.username)
        if sts.status==1:
            return render(request,"organiserhme.html")
        else:
            return redirect('home')
    else:
        return redirect('home')

#addevents function
def addevents(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            ename=request.POST["ename"]
            etype=request.POST["type"]
            place=request.POST["place"]
            edate=request.POST["date"]
            time=request.POST["time"]
            amount=float(request.POST["amount"])
            desc=request.POST["desc"]
            
            #Quering the data to insert
            format_str = '%Y-%m-%d' # The format
            datetime_obj = datetime.datetime.strptime(edate, format_str)
            if  date.today() <= datetime_obj.date():
                if amount > 0:
                    evnt=Events.objects.create(ename=ename,etype=etype,place=place,edate=edate,etime=time,edesc=desc,orgusrname=request.user.username,amount=amount)
                    evnt.save()
                    messages.success(request,"Event inserted successfully")
                    return redirect('orghome')
                else:
                    messages.error(request,"Please enter a valid amount")
                    return redirect('orghome')
            else:
                messages.error(request,"Enter date greater than today")
                return redirect('orghome')
        else:
            return render(request,"addevents.html")
    else:
            return redirect('home')

def viewevnts(request):
    if request.user.is_authenticated:
        evnts=Events.objects.filter(orgusrname=request.user.username)
        return render(request,'myevents.html',{'evnts':evnts})
    else:
        return redirect('home')

def orgprof(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            contact=request.POST["cntctno"]
            orgno=request.POST["orgno"]
            orgname=request.POST["orgname"]
            orgdata=Evntorganisers.objects.filter(id=request.user.username)
            if orgdata.count()==0:
                orgudata=Evntorganisers.objects.create(id=request.user.username,contact=contact,org_name=orgname,org_no=orgno)
                messages.success(request,"Profile Updated Successfully")
                return redirect('orgprof')
            else:
                orgudata=Evntorganisers.objects.get(id=request.user.username)
                if len(contact)!=0:
                    orgudata.contact=contact
                if len(org_no)!=0:
                    orgudata.org_no=org_no
                if len(org_name)!=0:
                    orgudata.org_name=org_name
                orgudata.save()
                messages.success(request,"Profile Updated Successfully")
                return redirect('orgprof')      
        else:
            orgdata=Evntorganisers.objects.filter(id=request.user.username)
            return render(request,"orgprof.html",{'org':orgdata})
    else:
        return redirect('home')



def changepasswd(request):
    if request.method=='POST':
        newpasswd=request.POST["nwpassword"]
        cnfrmpwd=request.POST["cpassword"]
        if newpasswd==cnfrmpwd:
            u = User.objects.get(username=request.user.username)
            u.set_password('new password')
            u.save()
            messages.success(request,"Passwords changed successfully plz login again")
            return redirect('orgprof')
        else:
            messages.success(request,"Passwords doesn't matched")
            return redirect('orgprof')

    else:
        return redirect('orgprof')
     