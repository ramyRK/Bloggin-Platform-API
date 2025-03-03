from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import postSerializer
from .models import Post

@api_view(['GET','POST'])
def posts(request):
    if request.method=='GET':
        posts=Post.objects.all()
        category=request.query_params.get('category')
        search=request.query_params.get('title')
        tag=request.query_params.get('tags')
        if category:
            posts=posts.filter(category=category)
        if search :
            posts=posts.filter(title__contains=search)   
        if tag :
            posts=posts.filter(tags__contains=tag)
        serialzed_items=postSerializer(posts,many=True)
        return Response(serialzed_items.data)
    if request.method=='POST':
        serialzed_items=postSerializer(data=request.data)
        serialzed_items.is_valid(raise_exception=True)
        serialzed_items.save()
        return Response(serialzed_items.validated_data,status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'GET':
        serializer = postSerializer(post)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = postSerializer(post, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        post.delete()
        return Response({'message': 'POST DELETED'}, status=status.HTTP_204_NO_CONTENT)