from django.urls import path
from demoapp import views

app_name='demoapp'

urlpatterns=[

    path('projects/',views.projects,name='projects'),

]
