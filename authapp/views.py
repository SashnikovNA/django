from django.shortcuts import render, HttpResponseRedirect, reverse
from django.http import HttpResponse, HttpRequest
from .forms import LoginForm
from django.contrib import auth
from authapp.forms import ShopUserRegisterForm, ShopUserEditForm




# Create your views here.

def redirect_to_login(request: HttpRequest):
    return HttpResponseRedirect('/auth/login')

def login(request: HttpRequest):
    title = 'Войти на сайт'

                            #Создаем форму чтобы заполнить
    login_form = LoginForm(data=request.POST)
                            #проверка данных из request
    if request.method == 'POST' and login_form.is_valid():
        login = request.POST['username']
        password = request.POST['password']
                            #выполнить аутентификацию
        user = auth.authenticate(username=login, password=password)

        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/')

    content = {
        'title': title,
        'login_form' : login_form
    }
    return render(request, 'authapp/login.html', content)

def logout(request: HttpRequest):
    auth.logout(request)
    return HttpResponseRedirect('/')

# def register (request):
#     return HttpResponseRedirect(reverse('main'))
# def edit (request):
#     return HttpResponseRedirect(reverse('main'))

def register(request):
    title = 'Регистрация'

    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
        else:
            register_form = ShopUserRegisterForm()

        content = {'title': title, 'register_form': register_form}

        return render(request, 'authapp/register.html', content)

def edit (request):
    title = 'редактирование'

    if request.method == 'POST' :
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse( 'auth:edit' ))
    else :
        edit_form = ShopUserEditForm(instance=request.user)
    content = {'title': title, 'edit_form': edit_form}
    return render(request, 'authapp/edit.html', content)
