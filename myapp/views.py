from django.shortcuts import  redirect, render
from myapp.models import signup_master,adduser
from .forms import signupForm,adduserForm
from django.contrib.auth import logout


# Create your views here.

def index(request):
    if request.method=='POST':
        unm=request.POST['email']
        pas=request.POST['password']
        user=signup_master.objects.filter(email=unm,password=pas)
        if user: #true
            print("Login Successfully!")
            request.session['user']=unm
            return redirect('home')
        else:
            print("Error...Login fail!")
    return render(request,'index.html')

def usersignup(request):
     if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")
            return redirect('home')
        else:
            print(newuser.errors)
     return render(request,'usersignup.html')

# def loginuser(request):
#      cuser=request.session.get('user')
#      return render(request,'home.html',{'user':cuser})

def userlogout(request):
    logout(request)
    return redirect("/")

def newuser(request):
    user=request.session.get('user')
    if request.method=='POST':
        mynote=adduserForm(request.POST)
        if mynote.is_valid():
            mynote.save()
            print("Your data has been submitted!")
            return redirect('home')
        else:
            print(mynote.errors)
    return render(request,'newuser.html',{'user':user})

def home(request):
    user=request.session.get('user')
    data=adduser.objects.all()
    print(data)
    return render(request,'home.html',{'data':data,'user':user})


def deletedata(request,stid):
   id=adduser.objects.get(id=stid)
   adduser.delete(id)
   return redirect('home')

def updatedata(request,stid):
    id=adduser.objects.get(id=stid)
    if request.method=='POST':
        updateuser=adduser(request.POST)
        if updateuser.is_valid():
            updateuser=adduserForm(request.POST,instance=id)
            updateuser.save()
            print("Your records has been updated!")
            return redirect('showdata')
        else:
            print(updateuser.errors)
    return render(request,'update.html',{'stdata':adduser.objects.get(id=stid)})