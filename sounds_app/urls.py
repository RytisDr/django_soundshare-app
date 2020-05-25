from django.urls import path, include
from . import views
#from .api import TodoList, TodoDetail

app_name = 'sounds_app'

urlpatterns = [
    #path('api/v1/', TodoList.as_view()),
    #path('api/v1/<int:pk>/', TodoDetail.as_view()),
    path('v1/rest-auth/', include('rest_auth.urls')),
    path('v1/rest-auth/registration/', include('rest_auth.registration.urls'))
]
