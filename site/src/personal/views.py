from operator import attrgetter
from django.shortcuts import render
from blog.models import BlogPost


def render_home_view(request):
    """ Home page """
    context = {}
    blog_posts = sorted(BlogPost.objects.all(),
                        key=attrgetter('date_updated'), reverse=True)  # library
    context['blog_posts'] = blog_posts

    return render(request, "personal/index.html", context)
