from django.urls import path
from app1 import views

#TEMPLATE URLs
app_name = 'app1'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('userLogin/',views.userLogin,name='userLogin')
]
