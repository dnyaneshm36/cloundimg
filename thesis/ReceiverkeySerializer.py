

from rest_framework import serializers

from .models import Receiverkey

class ReceiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receiverkey
        fields = [
            'id',
            'socialaccount',
            'clientsecrete',
            'sks',
            'pks'
        ]