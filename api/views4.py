from rest_framework import mixins
from rest_framework import generics
from rest_framework import permissions

from api.models import Music
from api.serializers import MusicSerializer

# Create your views here.
# https://q1mi.github.io/Django-REST-framework-documentation/tutorial/5-relationships-and-hyperlinked-apis_zh/


from api.permission import IsOwnerOrReadOnly


class MusicList(generics.ListCreateAPIView):   
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serilizer):
        serilizer.save(owner=self.request.user)


class MusicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly)


from django.contrib.auth.models import User
from api.serializers import UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'musics': reverse('music-list', request=request, format=format)
    })



from rest_framework import renderers


class MusicHighlight(generics.GenericAPIView):
    queryset = Music.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        music = self.get_object()
        return Response(music.highlighted)
