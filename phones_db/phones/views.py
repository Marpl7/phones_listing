from django.shortcuts import render, redirect
from .models import Phone



def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sorting = request.GET.get('sort', '?')
    if sorting == 'max_price':
        sorting = '-price'
    elif sorting == 'min_price':
        sorting = 'price'
    elif sorting == 'name':
        sorting = 'name'

    phones = Phone.objects.order_by(sorting)

    context = {

        'phones': phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {

        'phone': phone
    }
    return render(request, template, context)
