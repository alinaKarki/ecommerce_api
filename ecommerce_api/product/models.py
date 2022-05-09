from django.db import models

from ecommerce_api.users.models import User

# Create your models here.


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class CategoryModel(TimeStampModel):
    category_user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="category_user", default=None
    )
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)


class ProductsModel(TimeStampModel):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    category = models.ForeignKey(
        CategoryModel, on_delete=models.CASCADE, related_name="category"
    )
    price = models.FloatField()
    image = models.ImageField(blank=True, upload_to="static/")
    quantity = models.FloatField(default=0)


class Invoice(TimeStampModel):
    class IntergerEnum(models.IntegerChoices):
        First = 1, "Unpaid"
        Second = 2, "Paid"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="invoices")
    product = models.ForeignKey(
        ProductsModel,
        on_delete=models.CASCADE,
        related_name="invoice_product",
        default="0",
        null=True,
    )
    bill_number = models.CharField(max_length=30)
    status = models.PositiveSmallIntegerField(
        choices=IntergerEnum.choices, default=IntergerEnum.Second
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)


class Order(models.Model):
    invoice = models.ForeignKey(
        Invoice, on_delete=models.CASCADE, related_name="invoice"
    )
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    phone_number = models.BigIntegerField()

    def __str__(self):
        return self.name
