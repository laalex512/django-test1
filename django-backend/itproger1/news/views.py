from django.shortcuts import render

from .serializers import ArticleSerializer
from .models import Article
from django.contrib.auth.models import User
from .forms import ArticleForm
from django.views.generic import DetailView
from .models import Article

from rest_framework.viewsets import ModelViewSet

# Create your views here.


def news_home(request):
    news = Article.objects.all()
    context = {"title": "News", "news": news}
    return render(request, "news/index.html", context)


class ApiNewsView(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


def news_api(request):
    return render(request, "news/news_api.html")


def news1(request):
    context = {"title": "News #"}
    return render(request, "news/news1.html", context)


def create(request):
    message = ""
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Article added successfully"
        else:
            message = "Form incorrect"

    users = User.objects.all()
    form = ArticleForm()
    context = {
        "title": "Create new article",
        "users": users,
        "form": form,
        "message": message,
    }
    return render(request, "news/create.html", context)


class NewsSingleView(DetailView):
    model = Article
    template_name = "news/news1.html"
    context_object_name = "article"
