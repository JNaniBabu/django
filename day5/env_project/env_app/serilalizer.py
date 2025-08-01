from rest_framework import serializers
from .models import Sample_table

class sample_serializer(serializers.ModelSerializer):
    class Meta:
        model=Sample_table
        fields=["name",'mobile']
