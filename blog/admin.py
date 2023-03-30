from django.contrib import admin
from .models import Article, Category
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'parent', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    #وقتی تایتل ا میسازیم،اسلاگ رو خود به خود ایجاد میکند البته برای زبان انگلیسی مناسب هست
    #prepopulated_fields = {'slug':('title',)
admin.site.register(Category, CategoryAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish', 'status', 'category_to_str')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    #وقتی تایتل ا میسازیم،اسلاگ رو خود به خود ایجاد میکند البته برای زبان انگلیسی مناسب هست
    #prepopulated_fields = {'slug':('title',)}
    ordering = ['status', 'publish']

    def category_to_str(self, obj):
        return "، ".join([category.title for category in obj.category_published()])
    category_to_str.short_description = "دسته بندی"
    
admin.site.register(Article, ArticleAdmin)