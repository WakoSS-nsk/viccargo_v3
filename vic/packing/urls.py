from django.urls import path
from . import views


app_name = 'packing'

urlpatterns = [
    path('', views.PackingView.as_view(), name='packing_options'),
]
