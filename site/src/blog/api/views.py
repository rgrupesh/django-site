from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from account.models import Account
from blog.models import BlogPost
from blog.api.serializers import BlogPostSerializers

@api_view(['GET',])
def api_detail_blog_view(request,slug):

    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)    

    serializer= BlogPostSerializers(blog_post)
    return Response(serializer.data)


@api_view(['PUT',])
def api_update_blog_view(request,slug):

    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BlogPostSerializers(blog_post, data=request.data)
    data ={}
    if serializer.is_valid():
        serializer.save()
        data['success'] = 'updated successfully'
        return Response(data=data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
def api_delete_blog_view(request,slug):

    try:
        blog_post = BlogPost.objects.get(slug=slug)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)            

    operation = blog_post.delete()
    if operation:
        data['success'] = 'deleted successfully'
        return Response(data=data)
    else:
        data['failure'] = 'delete failed'
        return Response(data=data)

@api_view(['POST',])
def api_create_blog_view(request):

    account= Account.objects.get(pk=1)

    blog_post = BlogPost(author=account)

    serializer = BlogPostSerializers(blog_post,data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status= status.HTTP_201_CREATED)
    else:
        return Response(serializer.data, status= status.HTTP_400_BAD_REQUEST)    




