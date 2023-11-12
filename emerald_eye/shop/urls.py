from django.urls import path
from . import views
from . views import *

urlpatterns = [
    path("add_art/", AddArt.as_view(), name="add_art"),
    path('shop/', ArtList.as_view(), name="shop"),
    path('', views.index, name="index"),
    path('cart/', views.cart, name="cart"),
    path('view/', views.view, name="view"),
    path('checkout/', views.checkout, name="checkout"),
]