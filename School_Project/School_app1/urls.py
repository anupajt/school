from .import views
from django.urls import path

# app_name='school_app1'

urlpatterns=[
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('details',views.details,name='details'),
    # path('confirm',views.confirm,name='confirm'),
    ]