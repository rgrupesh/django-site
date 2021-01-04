from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from account.models import Account
from blog.models import BlogPost
from blog.api.serializers import BlogPostSerializers


@api_view(['GET', ])
@permission_classes((IsAuthenticated,))
def api_detail_blog_view(request, slug):

    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BlogPostSerializers(blog_post)
    return Response(serializer.data)


@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def api_update_blog_view(request, slug):

    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if blog_post.author != user:
        return Response({'response': "You don't have permission to update blog"})

    serializer = BlogPostSerializers(blog_post, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data['success'] = 'updated successfully'
        return Response(data=data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', ])
@permission_classes((IsAuthenticated,))
def api_delete_blog_view(request, slug):

    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    user = request.user
    if blog_post.author != user:
        return Response({'response': "You cannot delete blog"})

    operation = blog_post.delete()
    if operation:
        data['success'] = 'deleted successfully'
        return Response(data=data)
    else:
        data['failure'] = 'delete failed'
        return Response(data=data)


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def api_create_blog_view(request):

    account = request.user

    blog_post = BlogPost(author=account)

    serializer = BlogPostSerializers(blog_post, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
