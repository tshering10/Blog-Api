from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import Profile

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
            }
    
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already registered.")
        return value
        
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'], 
            password=validated_data['password'], 
        )
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Profile
        fields =['id', 'bio', 'user']
        
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)
        
        if user_data:
            for fields, value in user_data.items():
                setattr(instance.user, fields, value)
            instance.user.save()
            
            for fields, value in validated_data.items():
                setattr(instance, fields, value)
            instance.save()
            
            return instance
            