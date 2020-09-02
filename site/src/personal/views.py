from django.shortcuts import render
from account.models import Account

def render_home_view(request):

    context = {}

    users = Account.objects.all()
    context["users"] = users
    

    return render(request, "personal/index.html", context)
