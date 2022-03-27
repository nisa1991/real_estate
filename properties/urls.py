from django.urls import URLPattern, path
from .views import ListProperties

urlpatterns = [
    path('' , ListProperties.as_view(), name='properties')
]