from django.shortcuts import render
from store.models import Product


def home(request):

    # pido todos lo productos
    products = Product.objects.all().filter(is_available=True)

    # ahora, todo lo que me trae la busqueda me lo guardo en un diccionario
    context = {
        'products': products,
    }

    return render(request, 'home.html', context)
