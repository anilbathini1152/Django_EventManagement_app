from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError
from .models import IsOrganiser,Wbusers
from organiser.models import Events,Evntregistrations
from django.contrib.auth import authenticate, login, logout
def home(request):
    evnt=Events.objects.all()
    return render(request,"home.html",{'evnt':evnt})


# signup
def usignup(request):

    if request.method =='POST':
        try:
            #parameters gathering
            username=request.POST["username"]
            fname=request.POST["fname"]
            lname=request.POST["lname"]
            email=request.POST["email"]
            password=request.POST["password"]
            cpassword=request.POST["cpassword"]
            status=request.POST["category"]

            # validation of data
            # checking if username contains any other characters
            if username.isalnum():
                # checking if usrname len greater than 6
                if len(username)>=6:
                    # checking if password and conform password matched and password length
                    if len(password)>=8:
                        if password==cpassword:
                            myuser=User.objects.create_user(username=username,password=password,email=email)
                            myuser.first_name=fname
                            myuser.last_name=lname
                            myuser.save()
                            # saving in a seperate file to ensure if he is a organiser
                            isorg=IsOrganiser.objects.create(id=myuser.id,status=status,username=myuser.username)
                            isorg.save()
                            messages.success(request,"Registration success")
                            return redirect('home')
                        else:
                            messages.error(request,"Password and confirm password don't match")
                            return redirect('home')
                    else:
                        messages.error(request,"Password should be atleast 8 characters")
                        return redirect('home')
                else:
                    messages.error(request,"User name should be greater than 6 letters")
                    return redirect('home') 
            else:
                messages.error(request,"User name should contain only alphabets and numbers")
                return redirect('home')   
        except IntegrityError as e: 
                messages.error(request,"User name taken, try another")
                return redirect('home') 

    else:
        return HttpResponse("404 Page Not Found")

# Login
def ulogin(request):
    if request.method =='POST':
            #parameters gathering
            username=request.POST["username"]
            password=request.POST["password"]
            status=request.POST["category"]

            #organiser and user streams for login
            if status=='0':
                try:
                    validators=IsOrganiser.objects.get(username=username)
                except IsOrganiser.DoesNotExist:
                    messages.error(request,"Validation failed")
                    return redirect('home')
                if validators.status==0:
                    user=authenticate(username=username,password=password)
                    if user is not None:
                        login(request,user)
                        messages.success(request,"Successfully Logged in as "+str(user.username))
                        return redirect('home')
                    else:
                        messages.error(request,"invalid Credentials")
                        return redirect('home')
                else:
                    messages.error(request,"No user account with given credentials")
                    return redirect('home')
            else:
                try:
                    validators=IsOrganiser.objects.get(username=username)
                except IsOrganiser.DoesNotExist:
                    messages.error(request,"Validation failed")
                    return redirect('home')
                validators=IsOrganiser.objects.get(username=username)
                if validators.status==1:
                    user=authenticate(username=username,password=password)
                    if user is not None:
                        login(request,user)
                        messages.success(request,"Successfully Logged in as "+str(user.username))
                        return redirect('orghome')
                    else:
                        messages.error(request,"invalid Credentials")
                        return redirect('home')
                else:
                    messages.error(request,"No organiser account with given credentials")
                    return redirect('home')
    else:
        return HttpResponse("404 Page not found")

def ulogout(request):
        logout(request)
        messages.success(request,"Successfully Logged out")
        return redirect('home')

def uprof(request):
    usr=Wbusers.objects.filter(id=request.user.username)
    return render(request,'userprof.html',{'usr':usr})

def usrprofupdate(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            contact=request.POST["cntctno"]
            dob=request.POST["dob"]
            gender=request.POST["gendr"]
            vald=Wbusers.objects.filter(id=request.user.username)
            if not vald.exists():
                usrudata=Wbusers.objects.create(id=request.user.username,contact=contact,dob=dob,gender=gender)
                messages.success(request,"Profile Updated Successfully")
                return redirect('home')
            else:
                vald=Wbusers.objects.get(id=request.user.username)
                if len(contact)!=0:
                    vald.contact=contact
                if len(dob)!=0:
                    vald.dob=dob
                if len(gender)!=0:
                    vald.gender=gender
                vald.save()
                messages.success(request,"Profile Updated Successfully")
                return redirect('uprof')
        else:
            return HttpResponse('Page Not Found')
    else:
        return redirect('home')

def evntregister(request):
    if request.user.is_authenticated:   
        if request.method == 'GET':
            evntid = request.GET.get('evntid', None)
            query=Events.objects.get(evntid=evntid)
            #query = query.filter(evntid=evntid)
            reg=Evntregistrations.objects.create(evntid=evntid,ename=query.ename,username=request.user.username)
            messages.success(request,"Successfully Registered To Event")
            return redirect('home')
        else:
            return HttpResponse('Page Not Found')
    else:
        messages.success(request,"Login To Register")
        return redirect('home')


def myregistrations(request):
    if request.user.is_authenticated:
        evnts=Evntregistrations.objects.filter(username=request.user.username)
        # print(reg.values_list('evntid'))
        # evnts=Events.objects.filter(evntid__in=reg.values_list('evntid',flat=True))
        # print(evnts.values_list())
        # evnts=Events.objects.all()
        return render(request,'myregistrations.html',{'evnts':evnts})
    else:
        messages.success(request,"Login To View")
        return redirect('home')

def contactus(request):
    return render(request,'contactus.html')
