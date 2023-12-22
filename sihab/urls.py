from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView,LoginView

urlpatterns = [
    path('',views.sihab,name="Sihab"),
    path('Sihab',views.sihab,name="Sihab"),
]