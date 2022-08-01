from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"  # muestras todos los campos
        # exclude---cuando usas exclude no usas fields
    
    def to_representation(self,instance):
        return super().to_representation(instance)
    
    def create(self,validated_data):
        user_create=User(**validated_data)
        user_create.set_password(validated_data['password'])
        user_create.save()
        return user_create
    
    def update(self,instance,validated_data):
        user_update=super().update(instance,validated_data)
        user_update.set_password(instance,validated_data['password'])
        user_update.save()
        return user_update