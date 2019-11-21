from django.shortcuts import render
from rest_framework.response import Response

from user.serializer import *
# Create your views here.
from rest_framework.views import APIView


class RegisterAPIView(APIView):
    """用户注册"""

    def post(self, request):
        mes = {}
        data = request.data
        user = UserSerializer(data=data)
        if user:
            user.save()
            mes['code'] = 200
            mes['message'] = '注册成功'
        else:
            print(user.errors)
            mes['code'] = 1001
            mes['message'] = '注册失败'
        return Response(mes)


