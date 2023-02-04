from rest_framework import serializers
from .models import AdUnit, LineItem, Creative


class AdUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdUnit
        fields = '__all__'


class LineItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineItem
        fields = '__all__'


class CreativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Creative
        fields = '__all__'
