from django.urls import path

from .views import ShopPageView, SearchPageView

urlpatterns = [
    path('', ShopPageView.as_view(), name='Shop'),
    path('search', SearchPageView.as_view(), name='Search')
]