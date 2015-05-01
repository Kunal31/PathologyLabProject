from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.db import models
from labmanagement.models import UserProfile,Test,UserTest

class AccountModelForm(ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","username","email","password"]

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
    test_type = models.CharField(max_length=20)
    quantity = models.FloatField(max_length=10)
    color = models.CharField(max_length=20)
    appearance = models.CharField(max_length=20)
    reaction = models.CharField(max_length=25)                              
    cholestrol = models.FloatField(null=True,blank=True)                        # all 3 values in mg/dl
    ldl_cholestrol = models.FloatField(null=True,blank=True)
    triglycerides = models.FloatField(null=True,blank=True)

class UrineTestForm(forms.Form):
    test_type = models.CharField(max_length=20)
    quantity = models.FloatField(max_length=10)
    color = models.CharField(max_length=20)
    appearance = models.CharField(max_length=20)
    rbc = models.FloatField()                                                   # all 3 values in cells/HPF                                                   
    pus_cells = models.FloatField(null=True,blank=True)
    epithelial_cells = models.CharField(max_length=5,null=True,blank=True)
    
class SalivaTestForm(forms.Form):
    test_type = models.CharField(max_length=20)
    quantity = models.FloatField(max_length=10)
    color = models.CharField(max_length=20)
    appearance = models.CharField(max_length=20)
    estrone = models.FloatField(null=True,blank=True)                                               # all 3 values in pg/ml
    estradiol = models.FloatField(null=True,blank=True)
    progesterone = models.FloatField(null=True,blank=True)
    testosterone = models.FloatField(null=True,blank=True)
    
    