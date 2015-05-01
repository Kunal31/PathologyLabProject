from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class User(models.Model):
#     username = models.CharField(max_length=30)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.EmailField()
#    password = models.

class UserProfile(models.Model):
    """Extended model that store additional user details that are not present
    in django's auth_user model.
    
    """
    
    user = models.ForeignKey(User)
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'user_profile'
    
class Test(models.Model):
     
    test_type = models.CharField(max_length=20)
    quantity = models.FloatField(max_length=10)
    color = models.CharField(max_length=20)
    appearance = models.CharField(max_length=20)
    
    # blood test

#    Acidic = 'Acidic'
#    Basic = 'Basic'
#    Normal = 'Normal'
#    REACTION_CHOICES = ((Acidic,'Acidic'),(Basic,'Basic'),(Normal,'Normal'),)
#    Reaction = models.CharField(max_length=1,REACTION_CHOICES)
    
    reaction = models.CharField(max_length=25)                              
    cholestrol = models.FloatField(null=True,blank=True)                        # all 3 values in mg/dl
    ldl_cholestrol = models.FloatField(null=True,blank=True)
    triglycerides = models.FloatField(null=True,blank=True)
    
    #urine test
    rbc = models.FloatField()                                                   # all 3 values in cells/HPF                                                   
    pus_cells = models.FloatField(null=True,blank=True)
    epithelial_cells = models.CharField(max_length=5,null=True,blank=True)

    # saliva test
    estrone = models.FloatField(null=True,blank=True)                                               # all 3 values in pg/ml
    estradiol = models.FloatField(null=True,blank=True)
    progesterone = models.FloatField(null=True,blank=True)
    testosterone = models.FloatField(null=True,blank=True)
    
    def __str__(self):
        return self.test_type
    
    class Meta:
        db_table = 'test'
     
class UserTest(models.Model):
    
    patient = models.ForeignKey(User)
    test = models.ForeignKey(Test)
    
    class Meta:
        db_table = 'user_test' 
     
     
     
    
