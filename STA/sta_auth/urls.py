from django.urls import path, include
import sta_auth.views as views
from rest_framework.routers import DefaultRouter



urlpatterns = [

    # 这里需要末尾的 /
    path("signin/", views.SignIn.as_view()),
    path("signup/", views.SignUp.as_view()),
    path("signout/", views.SignOut.as_view()),

]