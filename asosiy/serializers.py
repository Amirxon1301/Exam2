from rest_framework import serializers
from .models import *
from rest_framework.exceptions import ValidationError

class MijozSerializer(serializers.Serializer):
    class Meta:
        model = Mijoz
        fields = '__all__'

class SuvSerializer(serializers.Serializer):
    class Meta:
        model = Suv
        fields = '__all__'

        def validate_litr(self, attrs):
            if attrs > 19:
                raise ValidationError("Bunday katta litrlarda suv sotilmaydi")


class AdminSerializer(serializers.Serializer):
    model = Admin
    fields = '__all__'

class HaydovchiSerializer(serializers.Serializer):
    model = Haydovchi
    fields = '__all__'

class BuyurtmaSerializer(serializers.Serializer):
    model = Buyurtma
    fields = '__all__'


