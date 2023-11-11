from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'shop/index.html')

def shop(request):
    context = {}
    return render(request, 'shop/shop.html')

def cart(request):
    context = {}
    return render(request, 'shop/cart.html')

def checkout(request):
    context = {}
    return render(request, 'shop/checkout.html')
