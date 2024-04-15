from .models import Article
from django.forms import ModelForm, TextInput, DateInput, Textarea


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["title", "announce", "content", "date_published"]

        widgets = {
            "title": TextInput(
                attrs={
                    "class": "form-control",
                    "id": "title_input",
                    "placeholder": "Title",
                }
            ),
            "announce": TextInput(
                attrs={
                    "class": "form-control",
                    "id": "announce_input",
                    "placeholder": "Announce",
                }
            ),
            "content": Textarea(
                attrs={
                    "class": "form-control",
                    "id": "floatingTextarea2",
                    "placeholder": "Text of Article",
                    "style": "height: 150px; margin-bottom: 20px",
                }
            ),
            "date_published": DateInput(
                attrs={
                    "class": "form-control",
                    "id": "date_input",
                    "placeholder": "Date published",
                }
            ),
        }
