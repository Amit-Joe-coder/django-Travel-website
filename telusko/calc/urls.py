from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('div',views.div,name='div'),
    path('sub',views.sub,name='sub'),
   
]