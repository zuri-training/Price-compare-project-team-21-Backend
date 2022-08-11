from django.urls import path
from . import views
from .views import Product, Category, Wishlist, Store
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('index', views.index, name = "index"),
    path('about', views.about, name = "about"),
    path('login', views.login, name = "login"),
    path('contact', views.contact, name = "contact"),
    path('privacy', views.privacy, name = "privacy"),
    path('term', views.term, name = "term"),
    path('accessories_category', views.accessories_category, name = "accessories_category"),
    path('laptop_category', views.laptop_category, name = "laptop_category"),
    path('phone_category', views.phone_category, name = "phone_category"),
	path('', Product),
    path('', Category),
    path('', Store),
    path('', Wishlist)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
