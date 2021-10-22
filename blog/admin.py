from django.contrib import admin
from .models import Article


# با استفاده از دکوریتور ادمین.رجبیسار میایم و هم کلاس ادمین و هم کلاس کاستومایز کردن ادمین رو فعال میکنیم
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'writer', 'slug', 'published', 'status')
    list_editable = ('status', )
    list_filter = ('status', 'published')
    search_fields = ('title', 'body')
    raw_id_fields = ('writer',) # زمانی که لیست دراپ دوون ما خیلی طولانی بشه، جلوه بدی پیدا میکنه. برای ایجاد یک حالت سرچ که بره اون مقدار مدنظر رو بیاره از این اتربیوت استفاده میکنیم
    prepopulated_fields = {'slug': ('title',)} # خیلی مفیده این اتر. میاد و یک فیلدی رو بر اساس یک فیلد دیگه پر میکنه. از نظر سئو هم حواسش هست. اگرکه در مدلمون بیایم و الوـیونیکد رو هم بدیم، فارسی رو هم ساپورت میکنه





