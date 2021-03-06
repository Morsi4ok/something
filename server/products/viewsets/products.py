from rest_framework.viewsets import ModelViewSet

from products.models import Product
from products.serializers.products import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
