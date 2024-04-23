from django.shortcuts import render
from django.db.models import Sum

from app_lection_05.models import Product


def total_in_db(request):
    total = Product.objects.aggregate(Sum('quantity'))
    context = {
        'title': 'Общее количество посчитано в базе данных',
        'total': total,
    }
    return render(request, 'app_lection_06/total_count.html', context)


def total_in_view(request):
    products = Product.objects.all()
    total = sum(product.quantity for product in products)
    context = {
        'title': 'Общее количество посчитано в представлении',
        'total': total,
    }
    return render(request, 'app_lection_06/total_count.html', context)


def total_in_template(request):
    context = {
    'title': 'Общее количество посчитано в шаблоне',
    'products': Product,
    }
    return render(request, 'app_lection_06/total_count.html', context)
