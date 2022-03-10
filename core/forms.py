from dataclasses import fields
from imp import init_builtin
from logging import PlaceHolder
from pyexpat import model
from random import choices
from aiohttp import request
from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.models import ( VICTIM_DETAILS, Gender_Choice,COUNCILLOR_DETAILS,CAMPS_DETAILS,
EVENT_DETAILS,SPONSER_DETAILS,BANNER_DETAILS,HELPER_DETAILS,EVENT_HELPER_DETAILS,CAMP_HELPER_DETAILS,
UPLOAD_DETAILS,FEEDBACK_DETAILS)


class signup(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Password')
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Password Confirmation')

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                'first_name':forms.TextInput(attrs={'class':'form-control'}),
                'last_name':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'})}

        labels={'email':'Email'}




class VictimForm(forms.ModelForm):
    Gender=forms.CharField(widget=forms.RadioSelect(choices=Gender_Choice))
    class Meta:
        model = VICTIM_DETAILS
        fields = '__all__'

        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Age':forms.NumberInput(attrs={'class':'form-control'}),
            'Address':forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3,'PlaceHolder':'Enter Your Address'}),
            'Contact':forms.NumberInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'Cuncilor_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Date_Of_Treatement':forms.SelectDateWidget()
        }
    
    def clean(self):
        cleaned_data=super().clean()
        contact=self.cleaned_data['Contact']
        if len(str(contact))!=10:
            raise forms.ValidationError('Please enter 10 digit Contact number!!')


class CouncillorForm(forms.ModelForm):
    Gender=forms.CharField(widget=forms.RadioSelect(choices=Gender_Choice))
    class Meta:
        model = COUNCILLOR_DETAILS
        fields = '__all__'

        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Address':forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3,'PlaceHolder':'Enter Your Address'}),
            'Contact':forms.NumberInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'Age':forms.NumberInput(attrs={'class':'form-control'}),
        }
    def clean(self):
        cleaned_data=super().clean()
        contact=self.cleaned_data['Contact']
        if len(str(contact))!=10:
            raise forms.ValidationError('Please enter 10 digit Contact number!!')
    

class CampForm(forms.ModelForm):
    class Meta:
        model = CAMPS_DETAILS
        fields = "__all__"
        widgets = {
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Address' : forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3,'PlaceHolder':'Enter Your Address'}),
            'DateOfCamps': forms.SelectDateWidget(),
            'Days_For_Camp': forms.NumberInput(attrs={'class':'form-control'}),
            'Number_Of_Monitors':forms.NumberInput(attrs={'class':'form-control'}),
            'Number_Of_Helpers':forms.NumberInput(attrs={'class':'form-control'}),
            'Need_Of_Helpers':forms.NumberInput(attrs={'class':'form-control'})
            }



class EventForm(forms.ModelForm):
    Gender=forms.CharField(widget=forms.RadioSelect(choices=Gender_Choice))
    class Meta:
        model = EVENT_DETAILS
        fields = '__all__'

        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Address':forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3,'PlaceHolder':'Enter Your Address'}),
            'Number_Of_Monitors':forms.NumberInput(attrs={'class':'form-control'}),
            'Number_Of_Helpers':forms.NumberInput(attrs={'class':'form-control'}),
            'Need_Of_Helpers':forms.NumberInput(attrs={'class':'form-control'}),
            'Date_Of_Events':forms.SelectDateWidget(),
        }
    

class SponcerForm(forms.ModelForm):
    class Meta:
        model = SPONSER_DETAILS
        fields = '__all__'

        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Address':forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3,'PlaceHolder':'Enter Your Address'}),
            'Contact':forms.NumberInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'Amount':forms.NumberInput(attrs={'class':'form-control'}),
        }
    def clean(self):
        cleaned_data=super().clean()
        contact=self.cleaned_data['Contact']
        if len(str(contact))!=10:
            raise forms.ValidationError('Please enter 10 digit Contact number!!')
        


class BannerForm(forms.ModelForm):
    class Meta:
        model = BANNER_DETAILS
        fields = '__all__'

        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Number_Of_Banner':forms.NumberInput(attrs={'class':'form-control'}),
            'Size_Of_Banner':forms.NumberInput(attrs={'class':'form-control'}),
            'Address':forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3,'PlaceHolder':'Enter Your Address'}),
        }
    


class HelperForm(forms.ModelForm):
    class Meta:
        model = HELPER_DETAILS
        fields = '__all__'

        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Address':forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3,'PlaceHolder':'Enter Your Full Address'}),
            'Contact':forms.NumberInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'Age':forms.NumberInput(attrs={'class':'form-control'}),
        }
    def clean(self):
        cleaned_data=super().clean()
        contact=self.cleaned_data['Contact']
        if len(str(contact))!=10:
            raise forms.ValidationError('Please enter 10 digit Contact number!!')


class HelperInEventForm(forms.ModelForm):
    class Meta:
        model = EVENT_HELPER_DETAILS
        fields = '__all__'

        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Event_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Contact':forms.NumberInput(attrs={'class':'form-control'}),
            'Monitor_Under':forms.TextInput(attrs={'class':'form-control'}),
        }
    def clean(self):
        cleaned_data=super().clean()
        contact=self.cleaned_data['Contact']
        if len(str(contact))!=10:
            raise forms.ValidationError('Please enter 10 digit Contact number!!')
    

class HelperInCampForm(forms.ModelForm):
    class Meta:
        model = CAMP_HELPER_DETAILS
        fields = '__all__'

        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'Camp_Name':forms.TextInput(attrs={'class':'form-control'}),
            'Contact':forms.NumberInput(attrs={'class':'form-control'}),
            'Monitor_Under':forms.TextInput(attrs={'class':'form-control'}),
        }
    def clean(self):
        cleaned_data=super().clean()
        contact=self.cleaned_data['Contact']
        if len(str(contact))!=10:
            raise forms.ValidationError('Please enter 10 digit Contact number!!')

class UploadForm(forms.ModelForm):
    class Meta:
        model = UPLOAD_DETAILS
        fields = '__all__'

        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control'}),
            'About_Image':forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3})
        }
            
       
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FEEDBACK_DETAILS
        fields = "__all__"
        widgets={
            'Name' : forms.TextInput(attrs={'class':'form-control'}),
            'Feedback': forms.Textarea(attrs={'class':'form-control','cols':1,'rows':3,'PlaceHolder':'Enter Your Feedback'})
        }
    
