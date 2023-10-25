from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from items.views import items_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('items.urls')),
    # re_path('', TemplateView.as_view(template_name='index.html')),
    path('', items_view, name='items'),
]
