from rest_framework import serializers
from .models import product
class ProductSerializer(serializers.Serializer):
    class Meta:
        models=product
        fields=('pid','pname')
