import stripe
from django.shortcuts import render
from django.core.mail import send_mail
import socket
from django.conf import settings
from django.db.models.query import QuerySet
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
)
from . models import *
import datetime
from . forms import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.sites.shortcuts import get_current_site



# Create your views here.

class ArtList(ListView):
    """
    View all available art
    """

    template_name = "shop/shop.html"
    model = Artwork
    context_object_name = "artwork"
    paginate_by = 6

    # Return only available art
    def get_queryset(self, **kwargs):
        artwork = self.model.objects.filter(
                Q(available='True')
            ).order_by('-date_added')
        return artwork

def index(request):
    context = {}
    return render(request, 'shop/index.html')

class ArtDetail(DetailView):
    """
    View details of artwork
    """

    template_name = "shop/art_detail.html"
    model = Artwork
    context_object_name = "art"

def cart(request):
    context = {}
    return render(request, 'shop/cart.html')

def checkout(request):
    context = {}
    return render(request, 'shop/checkout.html')


class AddArt(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """
    Add an artwork
    """

    template_name = "shop/add.html"
    context_object_name = "artwork"
    model = Artwork
    form_class = ArtForm
    success_url = "/shop/"
    success_message = 'Artwork Added To Catalog'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddArt, self).form_valid(form)
    
class EditArt(
        SuccessMessageMixin,
        LoginRequiredMixin,
        UserPassesTestMixin,
        UpdateView):
    """Edit Artwork"""

    template_name = "shop/edit.html"
    model = Artwork
    form_class = ArtForm
    success_message = 'Artwork Updated'

    def get_success_url(self):
        return reverse_lazy("art_detail", kwargs={"pk": self.object.pk})

    def test_func(self):
        return self.request.user.is_staff
    
class DeleteArt(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """Remove Artwork"""

    model = Artwork
    success_url = "/shop/"

    def test_func(self):
        return self.request.user.is_staff

    # For an unkown reason the SuccessMessageMixn is not working on Deleteview
    # even though it should be fixed per an issue
    # https://code.djangoproject.com/ticket/21936

    def post(self, request, *args, **kwargs):
        self.get_object().delete()
        messages.success(request, 'Artwork Deleted !!!')
        return redirect('/shop/')
    
class OrderList(UserPassesTestMixin, ListView):
    """
    View all art in order
    """

    def test_func(self):
        return self.request.user.is_authenticated
    
    def get(self, request, *args, **kwargs):
        order = Order.objects.get_or_create(customer=request.user, complete=False)[0]
        items = order.orderitem_set.all()
        total_price = sum(item.item.price for item in items)
        context = {'order': order, 'items': order.orderitem_set.all(), 'total_price': total_price}
        return render(request, 'shop/cart.html', context)
    
class AddToCartView(UserPassesTestMixin, ListView):

    def test_func(self):
        return self.request.user.is_authenticated

    def post(self, request, *args, **kwargs):
        order_id = Order.objects.get_or_create(customer=request.user, complete=False)[0]
        item_id = request.POST.get('product_id')
        artwork = Artwork.objects.get(id=item_id)
        orderitem, created = OrderItem.objects.get_or_create(
            order=order_id,
            item=artwork
        )
        return redirect('/cart/')
    
class DeleteCartItem(UserPassesTestMixin, DeleteView):
    """Remove item from cart"""

    model = OrderItem
    success_url = "cart/"

    def test_func(self):
        return self.request.user.is_authenticated

    # For an unkown reason the SuccessMessageMixn is not working on Deleteview
    # even though it should be fixed per an issue
    # https://code.djangoproject.com/ticket/21936

    def post(self, request, *args, **kwargs):
        self.get_object().delete()
        messages.success(request, 'Item removed from your cart')
        return redirect('cart')
    
#class ProcessOrder(ListView):

#     send_mail(
#     "Order Complete",
#     "Here is the message.",
#     "No_Reply@Emerald_Eye.com",
#     ["williamgriffithsireland@hotmail.com"],
#     fail_silently=False,
# )
    
def create_checkout_session(request):

    stripe.api_key = settings.STRIPE_API_KEY
    current_site = get_current_site(request)
    domain_name = current_site.domain

    order = Order.objects.get_or_create(customer=request.user, complete=False)[0]
    items = order.orderitem_set.all()
    total_price = sum(item.item.price for item in items) * 100

    try:
        checkout_session = stripe.checkout.Session.create(
            line_items=[{
            'price_data': {
                'currency': 'eur',
                'unit_amount': int(total_price),
                'product_data': {
                    'name': 'Emerald Eye Image Purchase',
                },
            },
            'quantity': 1,
        }],
        mode='payment',
        payment_method_types = ['card'],
        # PROD CODE
        # success_url = domain_name + '/shop',
        # cancel_url = domain_name + '/cart',
        # TEST CODE
        success_url = 'https://organic-space-lamp-9rp659xvp5pc76rx-8000.app.github.dev/shop',
        cancel_url = 'https://organic-space-lamp-9rp659xvp5pc76rx-8000.app.github.dev//cart',
        )
    except Exception as e:
        return redirect('cart')

    return redirect(checkout_session.url, code=303)