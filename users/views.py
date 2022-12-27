from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.models import User


def profile_view(request):
    return render(request, 'users/profile.html')


def upload_photo_view(request):
    photo = request.FILES.get('photo')
    user = request.user
    user.photo = photo
    user.save()
    return redirect('/users/profile')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        print(username, password)

        if username is None or password is None:
            messages.error(request, 'Введите все обязтелные данные')
            return redirect('/')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Успешная авторизация')
            return redirect('/')
        messages.error(request, 'Пароль или логин не правильный')
        return redirect('/')

    return render(request, 'users/login.html')


def register_user_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)

        if email is None or username is None or password is None:
            messages.error(request, 'Введите все обязтелные данные')
            return redirect('/')

        user = User.objects.create_user(username, email, password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Успешная авторизация')
            return redirect('/')

        messages.error(request, 'Ошибка при регистраций')
        return redirect('/')

    return render(request, 'users/register.html')


def logout_view(request):
    logout(request)
    return redirect('/')
