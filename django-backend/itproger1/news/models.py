from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField("Title", max_length=100)
    announce = models.CharField("Anounce", max_length=250)
    content = models.TextField("Content")
    date_published = models.DateTimeField("Date published")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "News"
