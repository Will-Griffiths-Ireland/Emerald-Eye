from django.urls import path
from . import views
from . views import *

urlpatterns = [
    path("add_art/", AddArt.as_view(), name="add_art"),
    path("art_edit/<slug:pk>/", EditArt.as_view(), name="art_edit"),
    path("art_delete/<slug:pk>/", DeleteArt.as_view(), name="art_delete"),
    path('shop/', ArtList.as_view(), name="shop"),
    path('sales/', ArtSales.as_view(), name="sales"),
    path('shop_search/', ArtSearch.as_view(), name="shop_search"),
    path('art_detail/<slug:pk>/', ArtDetail.as_view(), name="art_detail"),
    path('', views.index, name="index"),
    path('cart/', OrderList.as_view(), name="cart"),
    path('add_art_cart/', AddToCartView.as_view(), name='add_art_cart'),
    path('delete_cart_item/<slug:pk>/', DeleteCartItem.as_view(), name='delete_cart_item'),
    path('process_payment', views.create_checkout_session, name='process_payment'),
    path('order_complete/', views.order_complete, name='order_complete'),
]