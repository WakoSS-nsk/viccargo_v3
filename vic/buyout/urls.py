from django.urls import path
from . import views


app_name = 'buyout'

urlpatterns = [
    path('', views.BuyoutView.as_view(), name='buyout_options'),
]