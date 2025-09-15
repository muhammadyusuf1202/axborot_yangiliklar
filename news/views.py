from django.shortcuts import render, get_object_or_404
from .models import News

def home(request):
    category = request.GET.get('category')
    if category:
        news_list = News.objects.filter(category=category).order_by('-created_at')
    else:
        news_list = News.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'news_list': news_list})

def news_detail(request, pk):
    item = get_object_or_404(News, pk=pk)
    return render(request, 'detail.html', {'item': item})

def search_view(request):
    query = request.GET.get("q")
    results = []
    if query:
        results = News.objects.filter(title__icontains=query) | News.objects.filter(content__icontains=query)
    return render(request, "index.html", {"results": results, "query": query})

from django.shortcuts import render
from .models import News

def home(request):
    category = request.GET.get("category")
    if category:
        news_list = News.objects.filter(category=category).order_by("-created_at")
    else:
        news_list = News.objects.all().order_by("-created_at")
    return render(request, "index.html", {"news_list": news_list})


