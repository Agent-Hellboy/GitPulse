# app/views.py

from rest_framework import viewsets
from .models import Repository
from .serializers import RepositorySerializer

class RepositoryViewSet(viewsets.ModelViewSet):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer


from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to GitPulse! This is the root endpoint.")