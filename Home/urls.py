
from django.urls import path
from . import views

app_name = 'Home'

urlpatterns = [
    path('',views.Resume ,name ='Resume'),
    path('<str:slug>',views.Project_detail,name='Project_details'),
    path('success/',views.success ,name ='success'),
]