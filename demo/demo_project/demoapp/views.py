from django.shortcuts import render


def index(request):
    return render(request,'demoapp/index.html')
def projects(request):
    return render(request,'demoapp/projects.html')
