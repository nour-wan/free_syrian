from rest_framework import serializers
from .models import FreeName

class FreeNameSerializer(serializers.ModelSerializer):
    class Meta:
        model= FreeName
        fields = "__all__"