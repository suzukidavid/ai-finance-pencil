from rest_framework import generics
from .models import Income
from .serializers import IncomeSerializer


class IncomeList(generics.ListCreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class IncomeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
