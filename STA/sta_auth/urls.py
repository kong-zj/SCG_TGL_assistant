from django.urls import path, include
import sta_auth.views as views
from rest_framework.routers import DefaultRouter



urlpatterns = [

    # 这里需要末尾的 /
    path("login/", views.UserLogin.as_view()),
    path("register/", views.UserRegister.as_view()),
    path("setpwd/", views.UserSetpwd.as_view()),
    path("logout/", views.UserLogout.as_view()),

]