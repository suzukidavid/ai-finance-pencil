from django.urls import path
from .views import UserList

urlpatterns = [
    path('users/', UserList.as_view(), name='user_list'),
]
