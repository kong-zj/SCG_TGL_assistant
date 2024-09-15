from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.http import JsonResponse
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt


# 还有更简单的实现方法

# Django原生 CBV 编写API接口
class UserLogin(View):
    @csrf_exempt
    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
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
    

class UserRegister(View):
    @csrf_exempt
    def post(self, request):
        pass
    
    
class UserSetpwd(View):
    @csrf_exempt
    def post(self, request):
        pass
    

class UserLogout(View):
    @csrf_exempt
    def post(self, request):
        pass
    