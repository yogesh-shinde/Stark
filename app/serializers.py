from rest_framework import serializers
from .models import *

# AbstractUser
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'is_staff')


class AdminmodelSerializer(serializers.ModelSerializer):
    '''Create AdminmodelSerializer'''
    user = UserSerializer(required=False, allow_null=True)

    class Meta:
        model = Adminmodel
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        master, created = Adminmodel.objects.update_or_create(user=user
                                                              , gender=validated_data.pop('gender'))
        return master


class UsermodelSerializer(serializers.ModelSerializer):
    '''Create UsermodelSerializer'''
    user = UserSerializer(required=False, allow_null=True)

    class Meta:
        model = Usermodel
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        master, created = Usermodel.objects.update_or_create(user=user
                                                             , gender=validated_data.pop('gender'))
        return master

class MoviesSerializer(serializers.ModelSerializer):
    '''Create MoviesSerializer'''
    class Meta:
        model = Movies
        fields = '__all__'