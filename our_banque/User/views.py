from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import IsAuthenticated
from .models import ManagementUser
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from .serializers import RegisterUserSerializer, AutheticateUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken

"""
this view is used for Obtaining pair Token in JWT

"""
class UserTokenObtainPairView(TokenObtainPairView):
    pass

"""
this view is used for refreshing Token in JWT

"""
class UserTokenRefresh(TokenRefreshView):
    pass


"""
this view registe the user in database
"""
class RegisterUser(generics.CreateAPIView):
    queryset = ManagementUser
    serializer_class = RegisterUserSerializer
    
    
"""
this view manage the authentification of user and generate the access token and refresh token
"""
@api_view(["POST"])
def loginUserView(request, *args, **kwargs):
    if request.method == 'POST':
        serialized_data = AutheticateUserSerializer(data=request.data)
        if serialized_data.is_valid(raise_exception=True) :
            user = serialized_data.validated_data
            refresh_token = RefreshToken.for_user(user=user)
            access_token = refresh_token.access_token
            return Response({
                'acces_token':str(access_token),
                'refresh_token':str(refresh_token)
            },status=status.HTTP_200_OK )
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)