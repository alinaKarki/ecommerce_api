from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from yaml import serialize

from ecommerce_api.product.api.v1.serializers import (
    CategorySerializer,
    InvoiceSerializer,
    OrderSerializer,
    ProductSerializer,
)
from ecommerce_api.product.models import CategoryModel, Invoice, Order, ProductsModel

# Create your views here.


class CategoryViewSets(viewsets.ModelViewSet):

    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

    def list(self, request):

        queryset = CategoryModel.objects.all()
        # if list of queryset then many=True arguments is passed
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(category_user=request.category_user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        id = pk
        queryset = CategoryModel.objects.get(pk=id)
        queryset.delete()
        return Response({"msg: Successfully deleted"})

    def update(self, request, pk):
        id = pk
        queryset = CategoryModel.objects.get(pk=id)
        serializer = CategorySerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductView(APIView):
    def get(self, request):
        products = ProductsModel.objects.all()
        # if list of queryset then many=True arguments is passed
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InvoiceAPIView(APIView):
    def post(self, request):
        serializer = InvoiceSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request):
        products = Invoice.objects.all()
        # if list of queryset then many=True arguments is passed
        serializer = InvoiceSerializer(products, many=True)
        return Response(serializer.data)


class OrderViewSets(viewsets.ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def list(self, request):

        queryset = Order.objects.all()
        # if list of queryset then many=True arguments is passed
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        id = pk
        queryset = CategoryModel.objects.get(pk=id)
        queryset.delete()
        return Response({"msg: Successfully deleted"})

    def update(self, request, pk):
        id = pk
        queryset = CategoryModel.objects.get(pk=id)
        serializer = CategorySerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
