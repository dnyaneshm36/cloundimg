from rest_framework import serializers
from .models import Key


class KeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Key
        fields = [
            'id',
            'userid',
            'clientId',
            'qu',
            'du',
            'pku1',
            'pku2'
        ]

class PublicKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Key
        fields = [
            'du',
            'pku1',
            'pku2',
        ]