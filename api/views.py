from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.decorators import permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

#from mbr.models import Member,Membertype       #引用mbr.models,Membertype
from api.models import Member,Membertype,FriendShip
from api.serializers import MemberSerializer,MembertypeSerializer,FriendShipSerializer

# 設定權限，GET 時不用權限，POST 時需要權限

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    parser_classes = (JSONParser,)  # 只允許 Content-Type 是 application/json
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_permissions(self):
        if self.action in ('create',):
            self.permission_classes = [IsAuthenticated]
        return [permission() for permission in self.permission_classes]

    # [GET] api/member/
    def list(self, request, **kwargs):
        users = Member.objects.all()
        serializer = MemberSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # [POST] api/member/
    @permission_classes((IsAuthenticated,))
    def create(self, request, **kwargs):
        name = request.data.get('name')
        users = Member.objects.create(name=name)
        serializer = MemberSerializer(users)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MembertypeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Membertype.objects.all() #沒有錯誤!!
    serializer_class = MembertypeSerializer  
    parser_classes = (JSONParser,)      


class FriendShipViewSet(viewsets.ModelViewSet):
    queryset = FriendShip.objects.all() 
    serializer_class = FriendShipSerializer  
    parser_classes = (JSONParser,)    


def index(request):
    return render(request,'index.html')

