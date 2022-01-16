from django.forms.forms import Form
from django.http import request
from django.shortcuts import redirect,render,HttpResponse,get_object_or_404

import article
from .forms import ArticleForm,Article
from .models import Article,Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def articles(request):
    keyword= request.GET.get("keyword")

    if keyword:
        articles= Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})
    articles = Article.objects.all()
    return render (request,"articles.html",{"articles":articles})


def index(request):
    context = {
        "nu1": "Sayfaya Tam erişim için lütfen giriş yapın...",
    }
    return render(request, "index.html",context)

def about(request):
    return render(request, "about.html")

@login_required
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return render(request,"dashboard.html",context)
@login_required
def addArticle(request):
    form = ArticleForm(request.POST or None,request.FILES or None)

    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale Başarıyla Oluşturuldu.")
        return redirect("index")
    return render(request,"addarticle.html",{"form" :form})

def detail(request,id):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    article = get_object_or_404(Article,id = id)
    comments = article.comments.all()

    return render(request,"detail.html",{"article":article, "comments":comments})                                                                                                                                                                                                                                  

@login_required
def updateArticle(request,id):
    article = get_object_or_404(Article, id = id)
    form = ArticleForm(request.POST or None,request.FILES or None, instance = article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Makale Başarıyla Güncellendi.")
        return redirect("index")
    return render(request,"update.html",{"form":form})

@login_required
def deleteArticle(request,id):
    article = get_object_or_404(Article, id = id)

    article.delete()

    messages.success(request,"Makale Başarıyla Silindi...")
    return redirect("article:dashboard")

def addComment(request,id):
    article = get_object_or_404(Article, id = id)
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author = comment_author, comment_content = comment_content)
        newComment.article = article
        newComment.save()

    return redirect("/articles/article" + str(id))