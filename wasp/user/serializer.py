from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from user.models import *


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=12)  # 账号
    password = serializers.CharField()  # 密码
    phone = serializers.CharField(max_length=11)  # 手机号
    grade = serializers.IntegerField(allow_null=True)  # 用户等级
    email = serializers.EmailField(allow_null=True)  # 邮箱
    status = serializers.CharField(source='is_status')

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create(**validated_data)
        return user
