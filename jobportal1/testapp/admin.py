from django.contrib import admin
from .models import ApplicantData,jobdesc
# Register your models here.
class ApplicationDataAdmin(admin.ModelAdmin):
    list_display = ['name','email','mobile','qualification','resume','experience']
class jobdescAdmin(admin.ModelAdmin):
    list_display =['jobname','description','experience','qualification']
class applicationsAdmin(admin.ModelAdmin):
    list_display = ['applicant','email','mobile','qualification','resume','experience']

admin.site.register(ApplicantData,ApplicationDataAdmin)
admin.site.register(jobdesc,jobdescAdmin)
