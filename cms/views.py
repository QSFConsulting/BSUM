from django.shortcuts import render
from models import News
import os


def get_news(request):
    news_objects = News.objects.all().order_by("-updated")
    print os.path.join(
        os.path.dirname(__file__), 'static').replace('\\', '/')
    return render(request, 'index.html', {'news_objects': news_objects})
