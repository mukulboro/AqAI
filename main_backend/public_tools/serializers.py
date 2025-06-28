from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class RegisterManualSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    middle_name = serializers.CharField(required=False, allow_blank=True)
    
    class Meta:
        model = User
        fields = ("first_name", "middle_name", "last_name", "email", "password")
        
    def create(self, validated_data):
        user = User.objects.create_user(
            first_name = validated_data["first_name"],
            middle_name = validated_data["middle_name"],
            last_name = validated_data["last_name"],
            email = validated_data["email"],
            password = validated_data["password"],
        )
        return user
    
class RegisterGoogleSerializer(serializers.ModelSerializer):
    google_id_token = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ("google_id_token",)
        
    def create(self, validated_data):
        user = User.objects.create_user(
            first_name = validated_data["first_name"],
            middle_name = validated_data["middle_name"],
            last_name = validated_data["last_name"],
            email = validated_data["email"],
            password= "placeholderpassword123",
            is_google = True
        )
        user.set_unusable_password()
        return user
    
class LoginManualSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
class LoginGoogleSerializer(serializers.Serializer):
    google_id_token = serializers.CharField(write_only=True)       
        
        