from .models import reviews
from rest_framework import serializers


class ReviewsSerializer (serializers.ModelSerializer):
    class Meta:
        model = reviews
        fields ='__all__'