from django.shortcuts import render
'''
from api.models import Music
from api.serializers import MusicSerializer
'''
from rest_framework import viewsets

from api.models import Member
from api.serializers import MemberSerializer

# Create your views here.
'''
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
'''

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
 

def index(request):
    return render(request,'index.html')

