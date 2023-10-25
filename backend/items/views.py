from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Items
from .serializers import ItemsSerializer
from django.http import JsonResponse


class ItemsList(ListAPIView):
    queryset = Items.objects.filter(parent__isnull=True)
    serializer_class = ItemsSerializer


def items_view(request):
   data = [{'American Food': 10.99 }, {'Cheesy Prawns with corn': 10.99}, {'Cheese Burst Roll': 10.99}, {'Greeny Snails': 10.99}, {'Spicy Momos': 10.99}, {'Chicken Broast': 10.99}]

   return JsonResponse(data, safe=False)