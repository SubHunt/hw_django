from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_objects = Phone.objects.all()
    sort_pages = request.GET.get('sort')
    if sort_pages == 'name':
        phones_objects = phones_objects.order_by('name')
    elif sort_pages == 'min_price':
        phones_objects = phones_objects.order_by('price')
    elif sort_pages == 'max_price':
        phones_objects = phones_objects.order_by('price').reverse()

    context = {'phones': phones_objects,
               }
    print('show_c', phones_objects)
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    # phone = get_object_or_404(Phone, slug=slug)
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone,}
    print(phone.slug)
    return render(request, template, context)


