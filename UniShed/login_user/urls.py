from django.urls import path
from . import views

#TEMPLATE URLS!
app_name = 'login_user'

urlpatterns = [
    path('register/', views.register, name='register')
]

