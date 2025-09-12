from django.shortcuts import render, get_object_or_404
from .models import News

def home(request):
    category = request.GET.get("cat")
    if category:
        news_list = News.objects.filter(category=category).order_by("-created_at")
    else:
        news_list = News.objects.order_by("-created_at")
    return render(request, "index.html", {"news_list": news_list})

def detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, "detail.html", {"news": news})
