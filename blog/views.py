from django.shortcuts import render
from .models import Article


def all_articles(request):
    article = Article.objects.all()
    return render(request, 'blog/all_articles.html', {'all_articles': article,})
