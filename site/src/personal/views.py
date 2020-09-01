from django.shortcuts import render
from personal.models import Question

def render_home_view(request):

    context = {}

    questions = Question.objects.all()
    context["questions"] = questions

    return render(request, "personal/index.html", context)
