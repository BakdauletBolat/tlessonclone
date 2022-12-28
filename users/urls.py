from django.urls import path
from .views import (login_view, logout_view, profile_view,
                    upload_photo_view, register_user_view, users_view,
                    subscriptions_view, detail_user_view, request_user_view,
                    accept_user_view)

urlpatterns = [
    path('login/', login_view, name='login_users'),
    path('logout/', logout_view, name='logout_user', ),
    path('register/', register_user_view, name='register_users'),
    path('users/', users_view, name='users'),
    path('detail-user/<str:username>/', detail_user_view, name='detail_user'),
    path('subscriptions/<int:user_id>/', subscriptions_view, name='subscriptions'),
    path('request-user/<int:to_user_id>/', request_user_view, name='request_user'),
    path('accept-user/<int:request_user_id>/<int:statusAccept>/', accept_user_view, name='accept_user'),
    path('profile/', profile_view, name='profile'),
    path('upload-photo/', upload_photo_view, name='upload_photo')
]
