from rest_framework import serializers
from django.contrib.auth.models import User

from api.models import Music

class MusicSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
       model = Music
       fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    musics = serializers.PrimaryKeyRelatedField(many=True, queryset=Music.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'musics')


