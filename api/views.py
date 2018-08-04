from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers

from django.contrib.auth.models import User

from api.models import Music
from api.serializers import MusicSerializer,UserSerializer
from api.permission import IsOwnerOrReadOnly


# Create your views here.
# https://q1mi.github.io/Django-REST-framework-documentation/tutorial/6-viewsets-and-routers_zh/


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    此视图自动提供`list`和`detail`操作。
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer    


class MusicViewSet(viewsets.ModelViewSet):
    """
    此视图自动提供`list`，`create`，`retrieve`，`update`和`destroy`操作。

    另外我们还提供了一个额外的`highlight`操作。
    """
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)
    
    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        music = self.get_object()
        return Response(music.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)