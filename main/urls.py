from django.urls import path
from .views import ProductListViewMost, LoginView, register

urlpatterns = [
    path('', ProductListViewMost.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('reg/', register, name='reg'),
]