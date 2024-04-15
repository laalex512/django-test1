from os import name
from django.urls import path
from . import views

from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register("api", views.ApiNewsView)

urlpatterns = [
    path("", views.news_home, name="news_home"),
    path("news_api/", views.news_api, name="news_api"),
    path("create/", views.create, name="create_article"),
    path("<int:pk>", views.NewsSingleView.as_view(), name="news_single"),
]


urlpatterns += router.urls
