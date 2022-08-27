from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    # Главная страница
    path('', views.index, name='web_main'),
]
