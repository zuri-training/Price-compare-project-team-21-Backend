from django.urls import path
from . import views
#from .views import Product, Category, Wishlist, Store
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('index', views.index, name = "index"),
    path('about', views.about, name = "about"),
    path('contact', views.contact, name = "contact"),
    path('privacy', views.privacy, name = "privacy"),
    path('user_profile', views.user_profile, name = "user_profile"),
    path('term', views.term, name = "term"),
    path('review', views.review, name = "review"),
    path('wishlist', views.wishlist, name = "wishlist"),
    # path('accessories_category', views.accessories_category, name = "accessories_category"),
    path('accessory_category', views.all_accessory, name='all_accessory'),
    # path('laptop_category', views.laptop_category, name = "laptop_category"),
    path('laptop_category', views.all_laptops, name='all_laptops'),
    # path('phone_category', views.phone_category, name = "phone_category"),
    path('phone_category', views.all_phones, name='all_phones'),
	# path('', Product),
    # path('', Category),
    # path('', Store),
    # path('', Wishlist)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
