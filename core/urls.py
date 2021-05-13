from django.urls import path
from .views import AboutPageAPIView, IndexPageAPIView

urlpatterns = [
    path('about/', AboutPageAPIView.as_view(), name='about'),
    path('', IndexPageAPIView.as_view(), name='index'),
]
