from django.urls import path, include,re_path
from  .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "Authentication"

urlpatterns = [
    path('login/',UserSignup,name="login") 
]