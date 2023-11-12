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
    paginate_by = 4

    # Return only available art
    def get_queryset(self, **kwargs):
        artwork = self.model.objects.filter(
                Q(available='True')
            ).order_by('-date_added')
        return artwork

def index(request):
    context = {}
    return render(request, 'shop/index.html')

def view(request):
    context = {}
    return render(request, 'shop/view.html')

def cart(request):
    context = {}
    return render(request, 'shop/cart.html')

def checkout(request):
    context = {}
    return render(request, 'shop/checkout.html')


class AddArt(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """
    Add a page to the journal
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