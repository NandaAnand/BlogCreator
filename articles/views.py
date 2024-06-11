from django.shortcuts import render,redirect, get_object_or_404
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
import os

# Create your views here.

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request,'articles/article_list.html',{'articles':articles})

@login_required(login_url='/accounts/login/')
def article_my_list(request):
    articles = Article.objects.filter(author=request.user)
    return render(request,'articles/article_list.html',{'articles':articles})


def article_detail(request,slug):
    #return HttpResponse(slug)
    articles = Article.objects.filter(slug=slug)
    if articles.exists():
        article = articles.first()  # Or implement your logic to choose one article
        return render(request, 'articles/article_detail.html', {'article': article})
    else:
        # Handle the case where no article with the given slug exists
        return HttpResponseNotFound()


@login_required(login_url='/accounts/login/')
def article_create(request):
    if request.method == 'POST':
        form =forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request,'articles/article_create.html', {'form': form})

@login_required(login_url='/accounts/login/')
def article_edit(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES, instance=article)
        if form.is_valid():
            if 'thumb' not in request.FILES:
                form.instance.thumb = article.thumb  
            form.save()
            return redirect('articles:detail', slug=article.slug)
    else:
        form = forms.CreateArticle(instance=article)
    return render(request, 'articles/article_edit.html', {'form': form, 'article': article})

@login_required(login_url='/accounts/login/')
def article_delete(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:list')
    return render(request, 'articles/article_delete.html', {'article': article})

@csrf_exempt
def upload_image(request):
    if request.method == 'POST':
        print(request.method)
        image = request.FILES.get('file')
        print(image)
        if image:
            path = default_storage.save('uploads/' + image.name, image)
            image_url = default_storage.url(path)
            return JsonResponse({'location': image_url})
    return JsonResponse({'error': 'Image upload failed'}, status=400)