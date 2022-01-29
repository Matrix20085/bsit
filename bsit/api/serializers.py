from rest_framework import serializers
from .models import refineryJob


class refineryJobSerial(serializers.ModelSerializer):
    class Meta:
        model = refineryJob
        fields = '__all__'
