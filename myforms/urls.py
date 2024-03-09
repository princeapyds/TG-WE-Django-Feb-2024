from django.urls import path
from .views import my_form_view, success_view

urlpatterns = [
    path('my-form/', my_form_view, name='my_form'),
    path('success/', success_view, name='success'),
]
