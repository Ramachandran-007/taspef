from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Magazine
from .serializers import MagazineSerializer


class MagazineListView(APIView):
    def get(self, request):
        magazines = Magazine.objects.all().order_by('-date')
        serializer = MagazineSerializer(magazines, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
