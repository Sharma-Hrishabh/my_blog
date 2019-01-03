from django.shortcuts import render,redirect
from .models import Articles,Comment
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
from articles.config import pagination
from django.shortcuts import get_object_or_404

def article_list(request):
    articles=Articles.objects.all().order_by('date')
    pages=pagination(request,articles,2)

    context={'items':pages[0],
          'page_range':pages[1]
    }

    return render(request,'articles/article_list.html',context)

def article_detail(request,slug):
    #return HttpResponse(slug)
    article=Articles.objects.get(slug=slug)
    return render(request,'articles/article_detail.html',{'article':article })


@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method=='POST':
        form=forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author=request.user
            instance.save()            #save it
            return redirect('articles:list')

    else:
        form = forms.CreateArticle()
    return render(request,'articles/article_create.html',{'form':form})



def add_comment(request,slug):
    article = get_object_or_404(Articles,slug=slug)
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect('articles:list')
    else:
        form = forms.CommentForm()
    return render(request,'articles/add_comment.html',{'form':form})
