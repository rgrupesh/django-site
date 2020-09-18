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