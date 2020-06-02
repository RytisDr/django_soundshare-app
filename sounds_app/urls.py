from django.urls import path, include
from .api.account import registration, password_reset, password_reset_confirm, delete_account
from .api.sounds import post_sound, remove_sound, favorite_sound, unfavorite_sound, get_sounds, get_single_sound
# from .api import TodoList, TodoDetail

app_name = 'sounds_app'

urlpatterns = [
    path('v1/account/register/', registration, name='register'),
    path('v1/account/password/reset/', password_reset,
         name='password_reset'),
    path('v1/account/password/reset/confirm/', password_reset_confirm,
         name='password_reset_confirm'),
    path('v1/account/', include('rest_auth.urls')),
    path('v1/account/delete/', delete_account, name="delete_account"),
    path('v1/sounds/', get_sounds, name='get_sounds'),
    path('v1/sounds/<int:pk>/', get_single_sound, name='get_sounds'),
    path('v1/sounds/add/', post_sound, name='post_sound'),
    path('v1/sounds/remove/', remove_sound, name='remove_sound'),
    path('v1/sounds/favorite/', favorite_sound, name='favorite_sound'),
    path('v1/sounds/unfavorite/', unfavorite_sound, name='unfavorite_sound'),
]
