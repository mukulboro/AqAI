from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterManualSerializer, RegisterGoogleSerializer, LoginManualSerializer, LoginGoogleSerializer
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed

User = get_user_model()

class RegisterManualView(APIView):
    def post(self, request):
        serializer = RegisterManualSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        user = serializer.save()
        return Response({
            "success": "User Created Successfully",
            "user": RegisterManualSerializer(user).data
        }, status=status.HTTP_201_CREATED)
        
class RegisterGoogleView(APIView):
    def post(self, request):
        serializer = RegisterGoogleSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Do google magic
        validated_data = {
            "first_name": "Test",
            "last_name": "Best",
            "middle_name": None,
            "email": "west1q1@gmail.com"
        }
        user = serializer.create(validated_data)
        
        return Response({
            "success": "User Created Successfully",
            "user": RegisterManualSerializer(user).data
        }, status=status.HTTP_201_CREATED)

class LoginManualView(APIView):
    def post(self, request):
        serializer = LoginManualSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(**serializer.validated_data)
        
        if not user:
            raise AuthenticationFailed("Invalid Credentials")
        
        if not user.is_public:
            raise AuthenticationFailed("You do not have access with these credentials")
        
        refresh_token = RefreshToken.for_user(user)       
        
        return Response({
            "refresh_token": str(refresh_token),
            "access_token": str(refresh_token.access_token)
        })

class LoginGoogleView(APIView):
    def post(self, request):
        serializer = LoginGoogleSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        google_id_token = serializer.validated_data["google_id_token"]
        
        # Do google magic
        email = "west1q1@gmail.com"
        
        user = User.objects.filter(email=email)
        
        if not user:
            raise AuthenticationFailed("Invalid Credentials")
        
        user = user[0]
        
        if not user.is_public:
            raise AuthenticationFailed("You do not have access with these credentials")
        
        if not user.is_google:
            raise AuthenticationFailed("User was not registred using Google")
        
        refresh_token = RefreshToken.for_user(user)       
        
        return Response({
            "refresh_token": str(refresh_token),
            "access_token": str(refresh_token.access_token)
        })
        