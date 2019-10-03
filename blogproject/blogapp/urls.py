from django.urls import path
from . import views


urlpatterns=[

    path('',views.index,name='index'),
    path('category',views.category,name='category'),
    path('archive',views.archive,name='archive'),
    path('contact',views.contact,name='contact'),
    path('login',views.login,name='login'),
    


]