from django.urls import path
from . import views

app_name = 'budget'
urlpatterns = [
    path('test', views.hello_world, name='budget'),
]
