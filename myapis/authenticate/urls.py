from django.urls import path, include
from django.conf.urls import url
from . import views
urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    
]
