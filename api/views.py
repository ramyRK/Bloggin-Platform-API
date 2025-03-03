from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import postSerializer
from .models import post

@api_view(['GET','POST'])
def posts(request):
    if request.method=='GET':
        posts=post.objects.all()
        serialzed_items=postSerializer(posts,many=true)
        return Response(serialzed_items.data)
    if request.method=='POST':
        serialzed_items=postSerializer(data=request.data)
        serialzed_items.is_valid(raise_exception=True)
        serialzed_items.save()
        return Response(serialzed_items.validated_data,status.HTTP_201_CREATED)

api_view(['GET','DELETE','PUT'])
def post(request,pk):
    post = get_object_or_404(post,pk=pk)
    if request.method=='GET':
        serialized=postSerializer(post)
        return Response(serialized.data)
    if request.method=='PUT':
        serialized=postSerializer(post, data=request.data)
        serialized.is_valid(raise_exception=True)
        serialized.save()
        return Response(serialized.validated_data,status.HTTP_201_CREATED)
    if request.method=='DELETE':
        post.delete()
        return Response({'message':'POST DELETED'},status.HTTP_204_NO_CONTENT)