
from django.shortcuts import render, redirect
from login.models import Usertable
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
# Create your views here.
#显示登陆界面
def login(request):

    return render(request,'login_register/login.html')
#对登陆逻辑进行处理
def do_login(request):
    if request.method == "POST":
        username = request.POST.get('logname')
        psw = request.POST.get('logpass')
        user_object=Usertable.objects.filter(username=username)
        my_psw=''
        for i in user_object:
            my_psw=i.password
            print(my_psw)
        if check_password(psw,my_psw):
            return render(
                 request,
                "index/index.html",
                {'user':username}
                )
        elif username==''or psw=='':
            return render(
                request,
                'login_register/login.html',
                {'erormessage': '用户名或密码为空！'}
            )
        else:
            return render(
                request,
                'login_register/login.html',
                {'erormessage': '用户名或密码错误！'}
            )
#显示注册界面
def register(request):
    return render(request, 'login_register/regist.html')
#对注册逻辑进行处理
def do_register(request):
    if request.method=="GET":
        return render(request, 'login_register/regist.html')
    if request.method == "POST":
        username = request.POST.get('userName')
        psw = request.POST.get('pwd')
        psw1 = request.POST.get('pwd1')
        hash_psw=make_password(psw, None, 'pbkdf2_sha256')
        print(username)
        print(psw,psw1)
        if Usertable.objects.filter(username=username):
            return render(
                 request,
                "login_register/regist.html",
                {'message':'用户已经存在！'}
                )
        elif username=='' or  psw=='' or  psw1=='':
            return render(
                request,
                'login_register/regist.html',
                locals(),
                {'message': '用户名或密码为空！'}
            )
        else:
            Usertable(username=username,password=hash_psw).save()
            messages.success(request,"注册成功")
            return redirect('/login/')

