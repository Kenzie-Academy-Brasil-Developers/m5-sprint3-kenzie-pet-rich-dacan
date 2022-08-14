from rest_framework import serializers


class TraitSerializer(serializers.Serializer):
    name = serializers.CharField()
