from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("password/", views.password_page, name="password"),
    path("login/", views.login, name="login"),
    path("forgot-password/", views.forgot_password, name="forgot_password"),
    path("verify/", views.verify, name="verify"),
    path("new-password/", views.new_password, name="new_password"),
]