from rest_framework import serializers

class LogoutSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(max_length=700)
    
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=700)
    password = serializers.CharField(max_length=700)