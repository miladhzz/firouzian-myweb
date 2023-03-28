from django.contrib import admin
from .models import Article
# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'status')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    #وقتی تایتل ا میسازیم،اسلاگ رو خود به خود ایجاد میکند البته برای زبان انگلیسی مناسب هست
    #prepopulated_fields = {'slug':('title',)}
    ordering = ['status', 'publish']

admin.site.register(Article, ArticleAdmin)