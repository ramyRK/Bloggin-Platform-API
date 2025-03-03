from rest_framework import serializers
from .models import post

class postSerializer(serializers.ModelSerializer):
    class meta:
        model=post
        fields:'__all__'