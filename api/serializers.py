from rest_framework import serializers
from django.contrib.auth.models import User

from api.models import Music

class MusicSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='music-highlight',format='html')

    class Meta:
       model = Music
       fields = ('url', 'id', 'highlight', 'owner',
                'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    musics = serializers.HyperlinkedRelatedField(many=True, view_name='music-detail',read_only=True)    

    class Meta:
        model = User
        fields = ('url','id', 'is_superuser','username', 'email','musics')


