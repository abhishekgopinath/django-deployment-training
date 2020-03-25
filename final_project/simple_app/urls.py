from django.urls import path
from simple_app import views

app_name = 'simple_app'

urlpatterns = [
    path('register/', views.register, name='register')
]
