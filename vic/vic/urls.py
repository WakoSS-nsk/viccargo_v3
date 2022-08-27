from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('web.urls', namespace='web')),
    path('about/', include('about.urls', namespace='about')),
    path('buyout/', include('buyout.urls', namespace='buyout')),
    path('contacts/', include('contacts.urls', namespace='contacts')),
    path('delivery/', include('delivery.urls', namespace='delivery')),
    path('packing/', include('packing.urls', namespace='packing')),
    path('reviews/', include('reviews.urls', namespace='reviews')),
    path('search/', include('search.urls', namespace='search')),
]
