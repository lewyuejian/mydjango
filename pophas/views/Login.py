from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from pophas import models
from pophas.form.forms import UserForm
# 密码加密
import hashlib

def hash_code(s, salt='mydjango'):
    h=hashlib.sha256()
    s+=salt
    # update方法只接受bytes类型
    h.update(s.encode())
    return h.hexdigest()

def login(request):
    # if not request.session.get('is_login',None):
    #     return redirect('/login/')
    if request.session.get('is_login', None):  # 不允许重复登录
        return redirect('/index/')

    if request.method == 'POST':
        login_form=UserForm(request.POST)
        message='请检查填写的内容'
        if login_form.is_valid():
            username=login_form.cleaned_data['username']
            password=login_form.cleaned_data['password']
            try:
                user=models.User.objects.get(username=username)
                # 哈希值和数据库内的值进行比对
                if user.password == hash_code(password):
                    #if user.password == password:
                    request.session['is_login']=True
                    request.session['user_id']=user.id
                    request.session['user_name']=user.username
                    return redirect('/login/index/')
                else:
                    message='密码不正确'
            except:
                message='用户不存在'
        return render(request, 'login/login.html', locals())
    login_form=UserForm()

    return render(request, 'login/login.html', locals())


def index(request):

    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'login/index.html')


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')

    request.session.flush()
    # del request.session['is_login']
    return redirect("/login/")



