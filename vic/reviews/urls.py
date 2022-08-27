from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.ReviewsView.as_view(), name='reviews')
]
