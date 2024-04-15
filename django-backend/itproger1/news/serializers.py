from dataclasses import fields
from pyexpat import model
from rest_framework.serializers import ModelSerializer

from news.models import Article


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ["title", "announce", "content", "date_published"]
