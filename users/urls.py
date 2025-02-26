from django.urls import path
from . import views

from django.contrib.auth.views import (
    # PasswordResetView, # replaced with CustomPasswordResetView 
    PasswordResetDoneView, 
    PasswordResetConfirmView, 
    PasswordResetCompleteView
    )


urlpatterns = [
    path("register/", views.signup_page, name="register"),
    path("activate/<uidb64>/<token>/", views.activate_account, name="activate"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),

    # password-reset
    path("password-reset/", views.CustomPasswordResetView.as_view(), name="password_reset"),
    path("password-reset/done/", PasswordResetDoneView.as_view(template_name="pages/registration/password_reset_done.html"),  name="password_reset_done"),
    path("password-reset/confirm/<uidb64>/<token>/", PasswordResetConfirmView.as_view(template_name="pages/registration/password_confirm.html"), name="password_reset_confirm"),
    path("password-reset/complete/", PasswordResetCompleteView.as_view(template_name="pages/registration/password_reset_complete.html"), name="password_reset_complete"),
]

