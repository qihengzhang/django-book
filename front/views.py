from django.shortcuts import render
from .models import Users,Publisher
from django.http import HttpResponse
# Create your views here.

def index(request):
    #插入
    # user = Users(name='三国演义',author='Tom',price=200)
    # user.save()
    #删除
    # user = Users(id=1)
    # user.delete()
    #更新
    # user = Users.objects.get(pk=2)
    # user.price = 5000
    # user.save()
    #1.1查询(根据主键查询)
    # print(Users.objects.get(pk=2))
    #1.2查询(根据条件查找)
    # print(Users.objects.filter(author='Tom').first())

    return HttpResponse("三国演义")