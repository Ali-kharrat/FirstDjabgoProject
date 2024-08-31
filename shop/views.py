from django.shortcuts import render
from django.views.generic import ListView

# from add_cart.forms import AddCartForm
from main.models import Products
from django.db.models import Q


# Create your views here.
class ShopPageView(ListView):
    queryset = Products.objects.all()
    template_name = 'shop.html'
    paginate_by = 2


class SearchPageView(ListView):
    template_name = 'shop.html'
    paginate_by = 2

    def get_queryset(self):
        request = self.request.GET.get('q')
        return Products.objects.filter(Q(title__icontains=request) | Q(description__icontains=request))
