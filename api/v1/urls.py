from django.urls import include, path

app_name = "api_v1"

urlpatterns = [
    path(
        "products/", include("ecommerce_api.product.api.v1.urls", namespace="products")
    ),
    path("users/", include("ecommerce_api.users.api.v1.urls", namespace="user")),
]
