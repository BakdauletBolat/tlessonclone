from django.urls import path
from .views import login_view, logout_view, profile_view, upload_photo_view, register_user_view

urlpatterns = [
    path('login/', login_view, name='login_users'),
    path('logout/', logout_view, name='logout_user',),
    path('register/', register_user_view, name='register_users'),
    path('profile/', profile_view, name='profile'),
    path('upload-photo/', upload_photo_view, name='upload_photo')
]
