from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Artist, Albom, Songs
from .serializers import ArtistSerializer, AlbomSerializer, SongsSerializer

class LandingPageAPIView(APIView):
    def get(self, request):
        return Response(data={"get api": "Salom odamcha :)"})
    
    def post(self, request):
        return Response(data={"post api": "Bu yangi albom"})
    
class ArtistAPIView(APIView):
    def get(self, request):
        artists = Artist.objects.all()
        serializers = ArtistSerializer(artists, many=True)
        return Response(data=serializers.data)

class AlbomAPIView(APIView):
    def get(self, request):
        alboms = Albom.objects.all()
        serializers = AlbomSerializer(alboms, many=True)
        return Response(data=serializers.data)

class SongsAPIView(APIView):
    def get(self, request):
        songs = Songs.objects.all()
        serializers = SongsSerializer(songs, many=True)
        return Response(data=serializers.data)

