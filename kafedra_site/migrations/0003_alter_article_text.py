# Generated by Django 4.0 on 2022-01-21 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kafedra_site', '0002_article_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='text',
            field=models.TextField(max_length=1000, verbose_name='Содержание'),
        ),
    ]
