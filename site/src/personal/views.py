from django.shortcuts import render

def render_home_view(request):
    print(request.headers)
    return render(request, "base.html", {})
