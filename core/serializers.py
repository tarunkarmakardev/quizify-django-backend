from rest_framework import serializers
from .models import AboutPage, IndexPage


class AboutPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutPage
        fields = '__all__'


class IndexPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndexPage
        fields = '__all__'
