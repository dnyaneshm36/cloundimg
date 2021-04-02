from rest_framework import serializers
from .models import Senderkey


class SenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Senderkey
        fields = [
            'id',
            'socialaccount',
            'clientsecrete',
            'sks',
            'pks'
        ]