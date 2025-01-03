from django.urls import path
from .views import (UserTokenObtainPairView,
                    UserTokenRefresh,
                    RegisterUser,
                    loginUserView
                    )
""" the endpoint manage register of  user : http://127.0.0.1:8000/user/register
    the endpoint manage the authentifuication of user : http://127.0.0.1:8000/user/login
"""
urlpatterns = [
     path("api/token/", UserTokenObtainPairView.as_view(), name="userapitoken"),
    path("api/token/refresh/", UserTokenRefresh.as_view(), name="api_refresh_token"),
    path("register/", RegisterUser.as_view(), name="register-user"),
    path("login/", loginUserView, name="login-user"),
]
