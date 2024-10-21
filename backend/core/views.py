from django.shortcuts import render
from .models import User, User_Profile
from .serializers import UserSerializer, MyTokenObtainPairSerializer, SignInSerializer
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny, IsAuthenticated

class Obtain_Access_And_Refresh_tokens(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class SignIn_User(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = SignInSerializer

class DashboardView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        context = f"The is the Dashboard"
        return Response(context, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        response = f"Hello {request.user}! Here is your data {data}"
        return Response(response, status=status.HTTP_200_OK)
