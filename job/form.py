from django import forms
from .models import Apply , Job


class Apply_form(forms.ModelForm) :
    class Meta :
        model = Apply
        fields = ['name','email','website','cv','coverletter' ]
        

class Job_Form(forms.ModelForm):
    class Meta:


       model = Job
       fields = '__all__'
       exclude = ('slug','owner',)