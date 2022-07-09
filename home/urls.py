from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('sobre/', views.About.as_view(), name='sobre'),
    path('login/', views.Login.as_view(), name='login'),
    path('sair/', views.Sair.as_view(), name='sair'),
    path('signin/', views.Signin.as_view(), name='signin'),
]