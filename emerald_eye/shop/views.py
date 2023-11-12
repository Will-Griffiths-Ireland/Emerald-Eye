from django.shortcuts import render

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
    
class OrderList(LoginRequiredMixin, ListView):
    """
    View all available art
    """

    template_name = "shop/cart.html"
    model = Order
    context_object_name = "order"

    # Return only available art
    def get_queryset(self, **kwargs):
        cart = self.model.objects.filter(
                Q(self.request.user == Order.customer, Order.complete==False)
            ).order_by('-id')
        return cart