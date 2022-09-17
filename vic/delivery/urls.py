from django.urls import path
from . import views


app_name = 'delivery'

urlpatterns = [
    path('', views.DeliveryView.as_view(), name='delivery'),
    path('air/', views.AirDeliveryView.as_view(), name='air delivery'),
    path('road/', views.RoadDeliveryView.as_view(), name='road delivery'),
    path('train/', views.TrainDeliveryView.as_view(), name='train delivery'),
    path('ship/', views.ShipDeliveryView.as_view(), name='ship delivery'),
]
