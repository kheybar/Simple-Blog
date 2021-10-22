from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class PublishedArticleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='publish')



class Article(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('publish', 'Publish'),
    )

    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True, allow_unicode=True) # این الوـیونیکد به ما اجازه میده که اسلاگ فارسی رو هم در اپلیکیشن ساپورت کنه
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextUploadingField(config_name='awesome_ckeditor')
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS, default='draft')
    
    # customize Manager
    objects = models.Manager() # active default manager
    publish_filter = PublishedArticleManager() # customize manager


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:article_detail', args=(self.id, self.slug))







