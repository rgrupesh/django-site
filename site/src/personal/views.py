from django.shortcuts import render

def render_home_view(request):

    context = {}
    
    list_of_values = []
    list_of_values.append("First Number")
    list_of_values.append("second Number")
    list_of_values.append("third Number")
    list_of_values.append("Fourth Number")
    list_of_values.append("Fifth Number")

    context["list_of_values"] = list_of_values

    return render(request, "personal/index.html", context)
