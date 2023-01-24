from django.shortcuts import render
from .Serializers import companyserialzer
from rest_framework.generics import ListAPIView
from .models import company
# Create your views here.

class comapnyList(ListAPIView):
    queryset = company.objects.all()
    serializer_class = companyserialzer
    
