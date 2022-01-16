from django.db import models

import article



# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete=models.CASCADE, verbose_name = "Yazar")
    title = models.CharField(max_length= 50, verbose_name = "Başlık")
    content = models.TextField(verbose_name = "İçerik")
    created_date = models.DateTimeField(auto_now_add=True)
    article_image = models.FileField(blank = True,null = True,verbose_name="Makaleye Fotoğraf Ekleyin")
    def __str__(self):
        return self.title
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE, verbose_name= "Makale", related_name= "comments")
    comment_author = models.CharField(max_length= 20, verbose_name= "İsim")
    comment_content = models.CharField(max_length= 172, verbose_name= "Yorumunuz")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content