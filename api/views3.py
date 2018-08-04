from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from api.models import Music
from api.serializers import MusicSerializer

# Create your views here.
# http://www.chenxm.cc/post/291.html


class MusicList(APIView):
    # APIView实际继承django总的View
    # from django.views.generic import View
    """
    # 這裡是MusicList接口描述
    List all code musics, or create a new music.
    """
    def get(self, request, format=None):
        musics = Music.objects.all()
        # manay=True 用于querySet对象
        serializer = MusicSerializer(musics, many=True)
        # Respone比django的response更强大
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid():
            # .save()是调用MusicSerializer中的create()方法
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MusicDetail(APIView):
    """
    讀取, 更新 or 刪除一個程式片段(music)實例(instance).
    """
    def get_object(self, pk):
        try:
            return Music.objects.get(pk=pk)
        except Music.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        music = self.get_object(pk)
        serializer = MusicSerializer(music)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        music = self.get_object(pk)
        serializer = MusicSerializer(music, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        music = self.get_object(pk)
        music.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)