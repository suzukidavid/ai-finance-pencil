from rest_framework import generics
from .models import Expenses
from .serializers import ExpensesSerializer


class ExpensesList(generics.ListCreateAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer


class ExpensesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expenses.objects.all()
    serializer_class = ExpensesSerializer
