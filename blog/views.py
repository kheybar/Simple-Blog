from django.core.checks.messages import Error
from django.shortcuts import render, get_object_or_404
from .models import Article


def all_articles(request):
    article = Article.publish_filter.all() # use customize manager
    return render(request, 'blog/all_articles.html', {'all_articles': article,})


def article_detail(request, id, slug):
    article = get_object_or_404(Article, id=id, slug=slug)
    return render(request, 'blog/article_detail.html', {'article': article})



# filter or get?
# def article_detail(request, id, slug):

    # گت مستقیم میاد اطلاعات رو میریزه داخل متغییر. پس براحتی قابل دسترس هستند
    # گت برای زمانی هست که بخوایم یک آیتم رو از دیتابیس بیاریم و اگر شد چندتا، بهمون ارور میده
    # article = Article.objects.get(id=id, slug=slug)
    # print('*' * 90)
    # print(article) # install Manjaro


    # فیلتر اطلاعات رو میریزه داخل یک لیست و بعد به متغییر میده. پس برای اینکه در تمپلیت بهش دسترسی داشته باشیم باید روش حلقه ی فور بزنیم
    # چون لیست هست به راحتی میتونیم چند ایتم رو از دیتابیس بیاریم
    # article = Article.objects.filter(id=id, slug=slug)
    # print('*' * 90)
    # print(article) # <QuerySet [<Article: install Manjaro>]>


    # return render(request, 'blog/article_detail.html', {'article': article})