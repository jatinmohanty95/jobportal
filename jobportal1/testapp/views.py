from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.forms import CreateUserForm
from django.contrib import messages
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from.forms import jdform,applicantform
from.models import jobdesc,ApplicantData,applications
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
# Create your views here.






def freshview(request):
    return render(request, 'jobportal/fresh.html')



def homeview(request):
    appdat = ApplicantData.objects.all()
    context = {'appdat': appdat}
    print("===== Home context :: ",context)
    return render(request, 'jobportal/home.html',{'appdat':appdat,})

def createjob(request):
    form=jdform()
    if request.method=='POST':
        form=jdform(request.POST)
        if form.is_valid():
            jobname=request.POST.get('jobname')
            description=request.POST.get('description')
            experience=request.POST.get('experience')
            qualification=request.POST.get('qualification')
            data=jobdesc(
                jobname=jobname,
                description=description,
                experience=experience,
                qualification=qualification
            )
            data.save()
        form=jdform()
            # return redirect('/')
    context={'form':form}
    return render(request,'jobportal/jobform.html',context)

def applicant(request):
    applicant=ApplicantData.objects.all()
    form=applicantform()
    if request.method=="POST":
        form=applicantform(request.POST,request.FILES)
        if form.is_valid():
            name=request.POST.get('name')
            email=request.POST.get('email')
            mobile=request.POST.get('mobile')
            qualification=request.POST.get('qualification')
            resume=request.POST.get('resume')
            experience=request.POST.get('experience')
            data=applications(
                name=name,
                email=email,
                mobile=mobile,
                qualification=qualification,
                resume=resume,
                experience=experience
            )
            data.save()
            return HttpResponse("thanks for apply")
            # form=applicantform()
    context={'form':form,'applicant':applicant}
    return render(request,'jobportal/applicant.html',context)


def userpage(request):
    if request.method=='GET':
        jobdescr=jobdesc.objects.all()
        context={'jobdescr':jobdescr}
    # applicant=ApplicantData.objects.get(user=request.user)
        return render(request,'jobportal/user.html',context)
    else:return render(request,'jobportal/user.html',)




@unauthenticated_user
def registerpage(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=request.POST.get('username')
            messages.success(request,'Account Successfully Created' + user)
            redirect('login')
    context={'form':form}
    return render(request,'jobportal/register.html',context)


@unauthenticated_user
def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('fresh')
        else:
            messages.warning(request,'username or password is wrong')
    return render(request,'jobportal/login.html')
def logoutpage(request):
    logout(request)
    return redirect('login')


def applyjob(request):
    form=applicantform()
    if request.method=="POST":
        form=applicantform(request.POST, request.FILES)
        # print("====>> FORM data : ",form)
        if form.is_valid():

            # print('form is valid')
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'jobportal/applicationform.html', context)
