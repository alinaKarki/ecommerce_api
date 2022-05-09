from django.urls import path
from rest_framework.routers import DefaultRouter

from ecommerce_api.product.api.v1.views import (
    CategoryViewSets,
    InvoiceAPIView,
    ProductView,
)

app_name = "users_api_v1"

router = DefaultRouter()
router.register("category", CategoryViewSets)
# router.register("invoice",InvoiceAPIView)


urlpatterns = [
    path("invoice/", InvoiceAPIView.as_view(), name="invoice"),
    path("product/", ProductView.as_view(), name="product"),
]

urlpatterns += router.urls
