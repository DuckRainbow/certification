from rest_framework.serializers import ModelSerializer
from retailing.validators import SupplierValidator
from retailing.models import Supplier, Contact, Product


class SupplierSerializer(ModelSerializer):
    # Сериалайзер для всех views, кроме создания, модели Supplier
    class Meta:
        model = Supplier
        fields = '__all__'


class SupplierCreateSerializer(ModelSerializer):
    # Сериалайзер для создания модели Supplier
    class Meta:
        model = Supplier
        fields = ('title', 'contacts', 'products', 'supplier', 'debt', 'level')
        validators = [
            SupplierValidator(
                queryset=Supplier.objects.all(),
                field1='level',
                field2='supplier'
            )
        ]


class ContactSerializer(ModelSerializer):
    # Сериалайзер для модели Contact
    class Meta:
        model = Contact
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    # Сериалайзер для модели Product
    class Meta:
        model = Product
        fields = '__all__'
