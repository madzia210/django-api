
import sys
import time

import django

from django.conf import settings
from django.db import connection
from django.http import JsonResponse

from .models import Category, Product

APP_VERSION = "0.2.0"
START_TIME = time.time()


def json_response(data, status=200):
    return JsonResponse(
        data,
        safe=False,
        status=status,
        json_dumps_params={"ensure_ascii": False},
    )


def product_to_dict(product):
    return {
        "id": product.id,
        "name": product.name,
        "description": product.description,
        "price": str(product.price),
        "stock": product.stock,
        "category": product.category.name,
        "created_at": product.created_at.isoformat(),
    }


def health(request):
    try:
        connection.ensure_connection()
    except Exception:
        return json_response({"status": "error", "database": False}, status=503)

    return json_response({"status": "ok", "database": True})


def info(request):
    return json_response({
        "application": "Shop API",
        "app_version": APP_VERSION,
        "python_version": sys.version.split()[0],
        "django_version": django.get_version(),
        "data_source": {
            "type": "sqlite",
            "engine": settings.DATABASES["default"]["ENGINE"].split(".")[-1],
            "record_count": Product.objects.count(),
            "categories": list(
                Category.objects.order_by("name").values_list("name", flat=True)
            ),
        },
        "uptime_seconds": round(time.time() - START_TIME, 1),
    })


def product_list(request):
    products = Product.objects.select_related("category")

    category = request.GET.get("category")
    if category:
        products = products.filter(category__name=category)

    return json_response([product_to_dict(p) for p in products])


def product_detail(request, product_id):
    try:
        product = Product.objects.select_related("category").get(id=product_id)
    except Product.DoesNotExist:
        return json_response(
            {"error": f"Product {product_id} not found"},
            status=404,
        )

    return json_response(product_to_dict(product))


def statistics(request):
    products = Product.objects.all()

    categories = {}
    for product in products:
        name = product.category.name
        categories[name] = categories.get(name, 0) + 1

    prices = [product.price for product in products]

    return json_response({
        "total_products": products.count(),
        "categories": categories,
        "average_price": round(sum(prices) / len(prices), 2) if prices else 0,
        "min_price": min(prices) if prices else 0,
        "max_price": max(prices) if prices else 0,
    })
