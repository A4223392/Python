from django.shortcuts import render
from api.models import Member
from api.serializers import MemberSerializer

from rest_framework import viewsets
# Create your views here.

def index(request):
    return render(request,'index.html')

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer