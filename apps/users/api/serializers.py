from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"  # muestras todos los campos
        # exclude---cuando usas exclude no usas fields


class UsertestSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField()

    
    def validate_name(self, value):
        return value


    def validate_email(self, value):  
        return value

    def validate(self, data):
        return data
    
    def create(self,validated_data):
        return User.objects.create(**validated_data)
