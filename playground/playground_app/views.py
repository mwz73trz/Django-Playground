from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from playground_app.serializers import UserSerializer

# def index(request):
#     return HttpResponse("Hello, dear Reader.  This is the index of our app.")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
