from django.shortcuts import render
from models import News
import os


def get_index(request):
    news_objects = News.objects.all().order_by("-updated")[:2]
    for new in news_objects:
        new.cut = False
        if len(new.content):
            tmp_content = new.content[:360]
            tmp_content = " ".join(tmp_content.split(" ")[:-1]) + "..."
            new.content = tmp_content
            new.cut = True
    return render(request, 'index.html', {'news_objects': news_objects})


def get_news(request):
    news_objects = News.objects.all().order_by("-updated")
    return render(request, 'news.html', {'news_objects': news_objects})
