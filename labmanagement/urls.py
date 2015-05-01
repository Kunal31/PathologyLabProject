from django.conf.urls import patterns, url
from labmanagement import views

urlpatterns = patterns('',

#(?P<uid>\d+)
#this url is called when creating user account
url(r'^create_user/$', views.create_user,name='create_user'),

#this url is called when submitting test entry for patient
url(r'^create_test/$',views.create_test,name='create_test'),                       

#this url is called when generating test report for any user                       
url(r'^generate_report/$',views.generate_report,name='generate_report'),                       
)