from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from .models import Items

class ItemsSerializer(serializers.ModelSerializer):
    children = RecursiveField(many= True)
    class Meta:
        model = Items
        fields =('id', 'name', 'parent', 'children')