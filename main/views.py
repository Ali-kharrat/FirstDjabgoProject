from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, FormView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.http import Http404, HttpResponse
from django.contrib.auth.models import User

from .forms import RegisterUser, LoginUser
from .models import Users, Products


# Create your views here.
# @method_decorator(csrf_exempt, name='dispatch')
# class IndexView(TemplateView):
#     template_name = 'home.html'


@method_decorator(csrf_exempt, name='dispatch')
class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginUser
    success_url = '/'

    def form_valid(self, form):
        print('hello 65656')
        print(form.cleaned_data)
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        print(user)
        if user is not None:
            login(self.request, user)
            return redirect('/')
        else:
            raise Http404


def register(request):
    form = RegisterUser(request.POST or None)
    print(request.user.is_authenticated)
    if request.method == 'POST':
        print(form.is_valid())
        if form.is_valid():
            form.save()
            user = Users.objects.create(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password'],
                                        email=form.cleaned_data['email'],
                                        first_name=form.cleaned_data['first_name'],
                                        last_name=form.cleaned_data['last_name'],
                                        phone=form.cleaned_data['phone'],
                                        gender=form.cleaned_data['gender'],
                                        city=form.cleaned_data['city'])
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('/')
        else:
            print(form.errors)

    context = {'form': form}
    return render(request, 'register.html', context)


class ProductListViewMost(ListView):
    queryset = Products.objects.filter(most_sale=True).order_by("-id")[:3]
    print(queryset)
    template_name = 'home.html'
