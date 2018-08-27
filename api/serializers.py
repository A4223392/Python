from rest_framework import serializers

from api.models import Member,Membertype,FriendShip

class MemberSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Member
        fields = ('id','account','identifier','membertype','name','nickname','password','localpicture','dbpicture')
        #fields = '__all__'           


class MembertypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membertype
        fields = ('membertype_id','name','renew_time')


class FriendShipSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FriendShip       
        #field = ('member_id','friend_id','nickname','renew_time')
        fields = '__all__'