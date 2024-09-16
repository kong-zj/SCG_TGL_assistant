import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.http import JsonResponse
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt


# 还有更简单的实现方法

# Django原生 CBV 编写API接口
class SignIn(View):
    @csrf_exempt
    def post(self, request):
        # 注意 request.body 和 request.POST 的区别
        # username = request.POST.get('username', '')
        # password = request.POST.get('password', '')
        data = json.loads(request.body.decode('utf-8'))
        username = data.get('username')
        password = data.get('password')
        print(username)
        print(password)
        resUser:User = authenticate(request, username=username, password=password)
        if resUser and resUser.is_active:
            login(request, resUser)
            json_res = {
                'results': '登录成功'
            }
            return JsonResponse(json_res)
        else:
            json_res = {
                'results': '用户名或密码错误'
            }
            status_res = status.HTTP_401_UNAUTHORIZED
            return JsonResponse(json_res, status=status_res)
    

class SignUp(View):
    @csrf_exempt
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        print(username)
        print(password)
        print(email)
        resUser:User = authenticate(request, username=username, password=password)
        if resUser and resUser.is_active:
            login(request, resUser)
            json_res = {
                'results': '登录成功'
            }
            return JsonResponse(json_res)
        else:
            json_res = {
                'results': '用户名或密码错误'
            }
            status_res = status.HTTP_401_UNAUTHORIZED
            return JsonResponse(json_res, status=status_res)
    
    
class SignOut(View):
    @csrf_exempt
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        print(username)
        print(password)
        print(email)
        resUser:User = authenticate(request, username=username, password=password)
        if resUser and resUser.is_active:
            login(request, resUser)
            json_res = {
                'results': '登录成功'
            }
            return JsonResponse(json_res)
        else:
            json_res = {
                'results': '用户名或密码错误'
            }
            status_res = status.HTTP_401_UNAUTHORIZED
            return JsonResponse(json_res, status=status_res)
    

