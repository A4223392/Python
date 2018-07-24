from rest_framework import serializers
'''
from api.models import Music

class MusicSerializer(serializers.ModelSerializer):
   class Meta:
       model = Music
       fields = '__all__'
'''

from api.models import Member

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'