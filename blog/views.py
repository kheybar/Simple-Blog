from django.core.checks.messages import Error
from django.shortcuts import render, get_object_or_404
from .models import Article


def all_articles(request):
    article = Article.publish_filter.all() # use customize manager
    return render(request, 'blog/all_articles.html', {'all_articles': article,})


def article_detail(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/article_detail.html', {'article': article})
