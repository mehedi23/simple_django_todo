from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('sign-up/', views.sign_up, name="sign-up"),
    path('log-out/', views.log_out, name="log_out")
]