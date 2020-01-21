from rest_framework import serializers as sz
from rest_framework.settings import api_settings
from .models import MyUser


class GetFullUserSerializer(sz.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('id','username')

class UserSerializerWithToken(sz.ModelSerializer):
    password = sz.CharField(write_only=True)
    token = sz.SerializerMethodField()
    

    def get_token(self, object):
        jwt_payload_handler = api_settings.jwt_payload_handler
        jwt_encode_handler = api_settings.jwt_encode_handler

        payload = jwt_payload_handler(object)
        token = jwt_encode_handler(payload)

        return token

    def create(self, validated_data):
        user = MyUser.objects.create(
            username=validated_data['username'],
        )
        user.save()
        user.set_password(user.id, validated_data['password'])
        user.save()
        return user

    class Meta:
        model = MyUser
        fields = ('token', 'username', 'password')

    # def create(self, validated_data):
    #     profile = Profile.objects.create(
    #         username=validated_data['username'],
    #         name=validated_data['name'],
    #         gender=validated_data['gender'],
    #         email=validated_data['email'],
    #     )
    #     profile.set_hash_password(profle.id, validated_data['password'])
    #     profile.save()
    #     return profile

    # class Meta:
    #     model = Profile
    #     fields = ['token', 'username', 'password', 'name', 'gender', 'email']