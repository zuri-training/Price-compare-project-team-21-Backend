from django.urls import path
from . import views
from .views import Product, Category, Wishlist, Store
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('index', views.index, name = "index"),
	path('', Product),
    path('', Category),
    path('', Store),
    path('', Wishlist)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
