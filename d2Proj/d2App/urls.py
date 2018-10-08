from django.urls import path
from d2App import views

urlpatterns = [
    path('users/', views.users,name='users'),
]
