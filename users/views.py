from django.db.models import Case, When, Value, Q
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from users.models import User, UserRequest


def profile_view(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'users/profile.html', context)


def request_user_view(request, to_user_id):
    to_user = User.objects.get(id=to_user_id)
    user = request.user
    user.subscriptions.add(to_user.id)
    r = UserRequest.objects.create(
        to_user=to_user,
        from_user=user
    )

    return redirect(reverse('subscriptions', args=[user.id]))


def accept_user_view(request, request_user_id, statusAccept):
    user_request = UserRequest.objects.get(id=request_user_id)
    user_request.is_confirmed = True
    user_request.is_accept = statusAccept

    if statusAccept:
        to_user = user_request.to_user
        to_user.subscriptions.add(user_request.from_user.id)
        to_user.save()

    user_request.save()

    return redirect(reverse('subscriptions', args=[request.user.id]))


def detail_user_view(request, username):
    user = User.objects.get(username=username)
    context = {
        'user': user
    }
    return render(request, 'users/profile.html', context)


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


def users_view(request):
    users = User.objects.all().order_by('-id').annotate(
        text=Case(
            When(Q(subscribers__in=[request.user.id], subscriptions__in=[request.user.id]), then=Value('Вы друзья')),
            When(subscribers__in=[request.user.id], then=Value('Вы уже отправили запрос')),
            default=Value('Добавить в друзья'),
        )
    )

    context = {
        'users': users
    }

    return render(request, 'users/users.html', context)


def subscriptions_view(request, user_id):
    user = User.objects.get(id=user_id)
    subscriptions = user.subscriptions.all().annotate(
        text=Case(
            When(Q(subscribers__in=[request.user.id], subscriptions__in=[request.user.id]), then=Value('Вы друзья')),
            When(subscribers__in=[request.user.id], then=Value('Вы уже отправили запрос')),
            default=Value('Добавить в друзья'),
        )
    )

    context = {
        'user': user,
        'users': subscriptions
    }

    return render(request, 'users/users.html', context)
