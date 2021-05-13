from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import AboutPage, IndexPage
from .serializers import AboutPageSerializer, IndexPageSerializer


class IndexPageAPIView(ListAPIView):
    queryset = IndexPage.objects.all()
    serializer_class = IndexPageSerializer


class AboutPageAPIView(ListAPIView):
    queryset = AboutPage.objects.all()
    serializer_class = AboutPageSerializer
