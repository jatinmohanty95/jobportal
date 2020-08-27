from django import forms
from.models import jobdesc,ApplicantData
from django.contrib.auth.models import User
class jdform(forms.Form):
    jobname=forms.CharField(
        label="Enter jobname",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Jobname'
            }
        )
    )
    description=forms.CharField(
        label="Description",
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'description'
            }
        )

    )
    experience=forms.IntegerField(
        label='Experience(year)',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'enter experience'
            }
        )
    )
    qualification = forms.CharField(
        label='Qualification',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'enter qualification'
            }
        )

    )
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

class applicantform(forms.ModelForm):
    class Meta:
        model=ApplicantData
        fields=['name','email','mobile','qualification','resume','experience']
