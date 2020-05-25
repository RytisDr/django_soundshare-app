from django.urls import path, include
from .views import registration_view
# from .api import TodoList, TodoDetail

app_name = 'sounds_app'

urlpatterns = [
    # path('api/v1/', TodoList.as_view()),
    # path('api/v1/<int:pk>/', TodoDetail.as_view()),
    path('v1/account/', include('rest_auth.urls')),
    path('v1/account/register', registration_view, name='register')
]
