# Generated by Django 5.0.1 on 2024-01-16 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_article_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='date_created',
            new_name='date_published',
        ),
    ]
