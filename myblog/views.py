from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,reverse
def home(request):
    # return HttpResponse('home')
    return HttpResponseRedirect(reverse("articles:list"))
def about(request):
     #return HttpResponse('about')
    return render(request,'about.html')
