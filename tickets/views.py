from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status,viewsets
from . import serializers, models

@api_view(['GET','POST'])
def list_create_api_view(request):
    if request.method == 'GET':
        guests = models.Guest.objects.all()
        serializer = serializers.GuestSerializer(guests, many=True)
        # status=status.HTTP_201_CREATED
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = serializers.GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class MoveViewsetAPIView(viewsets.ModelViewSet):
    serializer_class = serializers.MovieSerializer
    queryset = models.Movie.objects.all()