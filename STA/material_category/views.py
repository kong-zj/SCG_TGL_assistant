import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer


def hello_world(request):
    return HttpResponse("HelloWorld")


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



# 模拟从数据库中查询到的数据
course_dict = {
    'name': '课程名称',
    'introduction': '课程介绍',
    'price': 0.11,
}

# Django原生 CBV 编写API接口
class CourseList(View):
    def get(self, request):
        return JsonResponse(course_dict)
    
    @csrf_exempt
    def post(self, request):
        course = json.loads(request.body.decode('utf-8'))
        return JsonResponse(course, safe=False)