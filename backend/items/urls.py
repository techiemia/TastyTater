from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('items/', views.ItemsList.as_view(), name='items-list'),
]