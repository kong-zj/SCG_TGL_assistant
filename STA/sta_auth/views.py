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
            # 用户登录成功之后（返回给客户端登录的凭证或者说是令牌、随机字符串）
            login(request, resUser)         # 自动操作django_session表
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
        # email = data.get('email')
        # 后续加入邮箱验证
        print(username)
        print(password)
        # print(email)
        # 校验username是否已被注册
        userList = User.objects.filter(username=username)
        userHasExist = False if len(userList)==0 else True
        print(userHasExist)
        if userHasExist:
            json_res = {
                'results': '用户名已存在，不能重复注册'
            }
            status_res = status.HTTP_406_NOT_ACCEPTABLE
            return JsonResponse(json_res, status=status_res)
        else:
            # 尝试注册
            try:
                User.objects.create_user(username=username, password=password)
            except Exception as ErrMessage:
                json_res = {
                    'detail': '注册失败，系统错误',
                    'errmessage': str(ErrMessage)
                }
                status_res = status.HTTP_406_NOT_ACCEPTABLE
                return JsonResponse(data=json_res,status=status_res)
            # 注册成功
            json_res = {
                'results': '注册成功'
            }
            return JsonResponse(data=json_res)
            
            

    
    
class SignOut(View):
    @csrf_exempt
    def post(self, request):
        try:
            logout(request)
        except Exception as ErrMessage:
            json_res = {
                'detail': '退出登录失败，系统错误',
                'errmessage': str(ErrMessage)
            }
            status_res = status.HTTP_406_NOT_ACCEPTABLE
            return JsonResponse(data=json_res,status=status_res)
        # 退出登录成功
        json_res = {
            'results': '退出登录成功'
        }
        return JsonResponse(data=json_res)
    

