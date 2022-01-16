from django.contrib import admin
from .models import Article,Comment

# Register your models here.

admin.site.register(Comment)

admin.site.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_date"]
    search_fields = ["title"]
    list_fileds = []
    
    
    class Meta:
        model = Article