from . import views
from django.urls import path


app_name = 'contacts'

urlpatterns = [
    path('', views.ContactsView.as_view(), name='contacts')
]
