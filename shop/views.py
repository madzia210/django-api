import sys
import time

import django
from django.http import JsonResponse

from .data import PRODUCTS


APP_VERSION = "0.1.0"
START_TIME = time.time()


def json_response(data, status=200):
    """Nasza wersja JsonResponse: obsługuje listy i nie ucieka polskich znaków."""
    return JsonResponse(
        data,
        safe=False,
        status=status,
        json_dumps_params={"ensure_ascii": False},
    )


def health(request):
    return json_response({"status": "ok"})


def info(request):
    return json_response({
        "application": "Shop API",
        "app_version": APP_VERSION,
        "python_version": sys.version.split()[0],
        "django_version": django.get_version(),
        "data_source": {
            "type": "in-memory list",
            "record_count": len(PRODUCTS),
            "categories": sorted({p["category"] for p in PRODUCTS}),
        },
        "uptime_seconds": round(time.time() - START_TIME, 1),
    })


def product_list(request):
    category = request.GET.get("category")

    if category:
        products = [
            p for p in PRODUCTS
            if p["category"] == category
        ]
    else:
        products = PRODUCTS

    return json_response(products)


def product_detail(request, product_id):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return json_response(product)

    return json_response(
        {"error": f"Product {product_id} not found"},
        status=404,
    )
def statistics(request):
    total_products = len(PRODUCTS)
    total_stock = sum(p["stock"] for p in PRODUCTS)

    prices = [p["price"] for p in PRODUCTS]

    return json_response({
        "total_products": total_products,
        "total_stock": total_stock,
        "average_price": round(sum(prices) / len(prices), 2),
        "categories": sorted({
            p["category"] for p in PRODUCTS
        }),
    })