from django.urls import path, include
from .api.account import registration, password_reset, password_reset_confirm, delete_account
from .api.sounds import post_sound_view
# from .api import TodoList, TodoDetail

app_name = 'sounds_app'

urlpatterns = [
    # path('api/v1/', TodoList.as_view()),
    # path('api/v1/<int:pk>/', TodoDetail.as_view()),
    path('v1/account/register/', registration, name='register'),
    path('v1/account/password/reset/confirm/', password_reset_confirm,
         name='password_reset_confirm'),
    path('v1/account/password/reset/', password_reset,
         name='password_reset'),
    path('v1/account/', include('rest_auth.urls')),
    path('v1/account/delete/', delete_account, name="delete_account"),
    path('v1/sounds/add/', post_sound_view, name='post_sound')
]
