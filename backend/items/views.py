from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Items
from .serializers import ItemsSerializer

class ItemsList(ListAPIView):
    queryset = Items.objects.filter(parent__isnull=True)
    serializer_class = ItemsSerializer