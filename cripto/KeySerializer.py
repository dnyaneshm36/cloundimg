from rest_framework import serializers
from .models import Key


class KeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Key
        fields = [
            'id',
            'socialaccount',
            'clientId',
            'qu',
            'du',
            'su',
            'sku1',
            'sku2',
            'pku1',
            'pku2'
        ]