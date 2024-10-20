from .models import User, User_Profile
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['email'] = user.email

        return token
    

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class SignInSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta: 
        models = User
        fields = ['email', 'username', 'password', 'password2']

    def validate(self, attrs):
        if (attrs['password'] != attrs['password2']):
            raise serializers.ValidationError({'Password', 'Password does not match'})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            useranme=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user