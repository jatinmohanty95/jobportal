from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('fresh/', views.freshview,name='fresh'),
    path('home/', views.homeview,name='home'),
    path('cjob/', views.createjob,name='cjob'),
    path('applicant/', views.applicant,name='customer'),
    path('register/',views.registerpage,name='register'),
    path('',views.loginpage,name='login'),
    path('logout/',views.logoutpage,name='logout'),
    path('user/',views.userpage,name='user-page'),
    path('applicant/',views.applicant,name='applicant'),
    path('applyjob/',views.applyjob,name='applyjob')
    ]
# login/
