from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db import models
from labmanagement.models import UserProfile,Test,UserTest

# class AccountModelForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ["first_name","last_name","username","email","password"]

class AccountForm(forms.Form):
    username = forms.CharField(max_length=30)
    first_name = forms.CharField()
    last_name = forms.CharField()
    password1 = forms.CharField(max_length=30, widget=forms.PasswordInput())  # render_value=False
    password2 = forms.CharField(max_length=30, widget=forms.PasswordInput())
    email = forms.EmailField(required=False)

    #title = forms.ChoiceField(choices=TITLE_CHOICES)

    def clean_username(self):  # check if username dos not exist before
        try:
            User.objects.get(username=self.cleaned_data['username'])  # get user from user model
        except User.DoesNotExist :
            return self.cleaned_data['username']
    
        raise forms.ValidationError("this user exist already")

    def clean(self):  # check if password 1 and password2 match each other
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:  # check if both pass first validation
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:  # check if they match each other
                raise forms.ValidationError("passwords dont match each other")
    
        return self.cleaned_data

    def save(self):  # create new user
        new_user = User.objects.create_user(username=self.cleaned_data['username'],
                                        last_name=self.cleaned_data['last_name'],
                                        password=self.cleaned_data['password1'])
        new_user.first_name = self.cleaned_data['first_name']
        new_user.last_name = self.cleaned_data['last_name']
        new_user.save() 
    
        return new_user

class BloodTestModelForm(ModelForm):
    class Meta:
        model = Test
        fields = ["test_type","quantity","color","appearance",
                  "reaction","cholestrol","ldl_cholestrol","triglycerides"]
        
class UrineTestModelForm(ModelForm):
    class Meta:
        model = Test
        fields = ["test_type","quantity","color","appearance",
                  "rbc","pus_cells","epithelial_cells"]
        
class SalivaTestModelForm(ModelForm):
    class Meta:
        model = Test
        fields = ["test_type","quantity","color","appearance",
                  "estrone","estradiol","progesterone","testosterone"]

class BloodTestForm(forms.Form):
    test_type = forms.CharField(max_length=20)
    quantity = forms.FloatField()
    color = forms.CharField(max_length=20)
    appearance = forms.CharField(max_length=20)
    reaction = forms.CharField(max_length=25)                              
    cholestrol = forms.FloatField()                        # all 3 values in mg/dl
    ldl_cholestrol = forms.FloatField()
    triglycerides = forms.FloatField()
    
    def save(self):  # create new user
        new_test = Test.objects.create(test_type=self.cleaned_data['test_type'],
                                        quantity=self.cleaned_data['quantity'],
                                        color=self.cleaned_data['color'],
                                        appearance=self.cleaned_data['appearance'],
                                        reaction=self.cleaned_data['reaction'],
                                        cholestrol=self.cleaned_data['cholestrol'],
                                        ldl_cholestrol=self.cleaned_data['ldl_cholestrol'],
                                        triglycerides=self.cleaned_data['triglycerides'])
        new_test.save() 


class UrineTestForm(forms.Form):
    test_type = forms.CharField(max_length=20)
    quantity = forms.FloatField()
    color = forms.CharField(max_length=20)
    appearance = forms.CharField(max_length=20)
    rbc = forms.FloatField()                                                   # all 3 values in cells/HPF                                                   
    pus_cells = forms.FloatField()
    epithelial_cells = forms.CharField(max_length=5)
    
class SalivaTestForm(forms.Form):
    test_type = forms.CharField(max_length=20)
    quantity = forms.FloatField()
    color = forms.CharField(max_length=20)
    appearance = forms.CharField(max_length=20)
    estrone = forms.FloatField()                                               # all 3 values in pg/ml
    estradiol = forms.FloatField()
    progesterone = forms.FloatField()
    testosterone = forms.FloatField()
    
    
