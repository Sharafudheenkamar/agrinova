from django import forms
from .models import *

class policyform(forms.ModelForm):
    class Meta:
        model=policy
        fields=['PolicyTitle','Category','Details','policyfile']

class feedbackform(forms.ModelForm):
    class Meta:
        model=feedback
        fields=['feedback','reply']

class complaintform(forms.ModelForm):
    class Meta:
        model=complaint
        fields=['complaint','reply','status']

class productform(forms.ModelForm):
    class Meta:
        model=product
        fields=['image','price','name','Details','Quantity']
    
class requestform(forms.ModelForm):
    class Meta:
        model=requesttable
        fields=['quantity','productid']

class cartform(forms.ModelForm):
    class Meta:
        model=cart
        fields=['productid','quantity']

class labourform(forms.ModelForm):
    class Meta:
        model=labour
        fields=['name','hour','task','status']

class farmerform(forms.ModelForm):
    class Meta:
        model=farmer
        fields=['name','address','place','mob_no','K_bhavan']
     
class  businessform(forms.ModelForm):
    class Meta:
        model=business
        fields=['name','address','place','mob_no']

class notificationform(forms.ModelForm):
     class Meta:
        model=notification
        fields=['notification']

class bcomplaintform(forms.ModelForm):
     class Meta:
        model=Bcomplaint
        fields=['name','email','Category','Details','docfile']    

    

    




