# Generated by Django 3.2.8 on 2021-10-22 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=150, unique=True),
        ),
    ]
