from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework import viewsets

from api.models import Music
from api.serializers import MusicSerializer

# Create your views here.
# http://www.chenxm.cc/post/289.html?segmentfault
'''CASE 1
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
'''
'''CASE 2
@csrf_exempt
def music_list(request):
    """
    List all code musics, or create a new music.
    """
    if request.method == 'GET':
        musics = Music.objects.all()
        serializer = MusicSerializer(musics, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MusicSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            # serializer.data 数据创建成功后所有数据
            return JsonResponse(serializer.data, status=201)
        # serializer.errors 错误信息
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def music_detail(request, pk):
    """
    Retrieve, update or delete a code music.
    """
    try:
        music = Music.objects.get(pk=pk)
    except Music.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MusicSerializer(music, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        music.delete()
        return HttpResponse(status=204)
'''
#CASE 3 with browser api
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET','POST'])
def music_list(request,format=None):
    """
    List all code musics, or create a new music.
    """
    if request.method == 'GET':
        musics = Music.objects.all()
        serializer = MusicSerializer(musics, many=True)
        return Response(serializer.data)  

    elif request.method == 'POST':       
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def music_detail(request, pk,format=None):
    """
    Retrieve, update or delete a code music.
    """
    try:
        music = Music.objects.get(pk=pk)
    except Music.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MusicSerializer(music)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MusicSerializer(music, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        music.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)