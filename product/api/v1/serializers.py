from rest_framework import serializers

from ecommerce_api.product.models import CategoryModel,  Invoice, Order, ProductsModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ["id","category_user", "name", "description", "created_at", "updated_at"]
        extra_kwargs = {
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }
        # read_only_fields = ('category_user',)
    
class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductsModel
        fields = '__all__'
        extra_kwargs = {
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }

        
       


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ('user','product','number', 'amount' )
        extra_kwargs = {
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('invoice','name', 'address', 'phonenumber')