
from django.contrib import admin
from django.urls import path,include
from demoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('demoapp/',include('demoapp.urls'))
]
