from django.shortcuts import render, render_to_response
from django.http import HttpResponse,HttpResponseServerError
from labmanagement import models
from labmanagement import forms
from labmanagement.forms import BloodTestForm
from django.template.context import RequestContext
from django.db.models.query_utils import Q
from django.core.exceptions import ObjectDoesNotExist

def create_user(request):
    if request.method == "POST":
        userform = forms.AccountModelForm(request.POST)
        if userform.is_valid():
            new_user = userform.save()
            return HttpResponse("saved")
        else:
            return HttpResponseServerError()
#     else:
#         form = AccountForm()
    
    return render(request,'*.html',{'userform': userform})

def create_test(request):
    if request.method == "POST":
        data = request.POST
        if data.has_key('blood'):
            testform = forms.BloodTestForm(request.POST)
            if testform.is_valid():
#                 test_type = testform.cleaned_data['test_type']
#                 quantity = testform.cleaned_data['quantity']
#                 color = testform.cleaned_data['color']
#                 appearance = testform.cleaned_data['appearance']
#                 reaction = testform.cleaned_data['reaction']                             
#                 cholestrol = testform.cleaned_data['cholestrol']                       # all 3 values in mg/dl
#                 ldl_cholestrol = testform.cleaned_data['ldl_cholestrol']
#                 triglycerides = testform.cleaned_data['triglycerides']
                testform.save()
                last_test = models.Test.objects.latest('id')
                usertest = models.UserTest.objects.create(request.user,last_test)
                return HttpResponse("saved")
        elif data.has_key('urine'):
            testform = forms.UrineTestForm(request.POST)
            if testform.is_valid():
#                 test_type = testform.cleaned_data['test_type']
#                 quantity = testform.cleaned_data['quantity']
#                 color = testform.cleaned_data['color']
#                 appearance = testform.cleaned_data['appearance']
#                 rbc = testform.cleaned_data['rbc']                                                   # all 3 values in cells/HPF                                                   
#                 pus_cells = testform.cleaned_data['pus_cells']
#                 epithelial_cells = testform.cleaned_data['epithelial_cells']
                testform.save()
                last_test = models.Test.objects.latest('id')
                usertest = models.UserTest.objects.create(request.user,last_test)
                return HttpResponse("saved")
        elif data.has_key('saliva'):
            test_form = forms.SalivaTestForm(request.POST)
            if testform.is_valid():
#                 test_type = testform.cleaned_data['test_type']
#                 quantity = testform.cleaned_data['quantity']
#                 color = testform.cleaned_data['color']
#                 appearance = testform.cleaned_data['appearance']
#                 estrone = testform.cleaned_data['estrone']                                               # all 3 values in pg/ml
#                 estradiol = testform.cleaned_data['estradiol']
#                 progesterone = testform.cleaned_data['progesterone']
#                 testosterone = testform.cleaned_data['testosterone']
                last_test = models.Test.objects.latest('id')
                models.UserTest.objects.create(request.user,last_test)
                testform.save()
                return HttpResponse("saved")
    else:
        testform = BloodTestForm()
    return render(request,'*.html',{'userform': testform})

def get_test_status(request):
    if request.method == 'POST':
        #user = models.User.objects.get(Q(username = request.POST.get("username")) | Q(username = request.POST.get("username")))
        try:   
            tests = models.Test.objects.filter(Q(patient_id = request.user.id) | Q(id = request.POST.get('receipt_no')))
        except ObjectDoesNotExist:
            return HttpResponseServerError()
        else:
            resp_dict = {tests:"tests"}
            render_to_response('*.html',resp_dict,context_instance=RequestContext(request))
            
            
         
    



