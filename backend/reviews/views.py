from django.shortcuts import render
from .models import reviews
from rest_framework import generics
from .serializers import ReviewsSerializer


class ReviewsList(generics.ListAPIView):
    queryset = reviews.objects.order_by('-created_at').all()
    serializer_class = ReviewsSerializer

class ReviewsAdd (generics.CreateAPIView):
    queryset = reviews.objects.all()
    serializer_class = ReviewsSerializer

class ReviewsDetail (generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = reviews.objects.all()
    serializer_class = ReviewsSerializer