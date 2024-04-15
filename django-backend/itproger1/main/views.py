from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"title": "Main page"}
    return render(request, "main/index.html", context)


def about(request):
    context = {"title": "About Us"}
    return render(request, "main/about.html", context)
