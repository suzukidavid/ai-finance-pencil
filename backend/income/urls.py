from django.urls import path
from .views import IncomeList, IncomeDetail

urlpatterns = [
    path('incomes/', IncomeList.as_view(), name='income_list'),
    path('incomes/<int:pk>/', IncomeDetail.as_view(), name='income_detail'),
]
