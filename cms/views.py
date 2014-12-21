from django.shortcuts import render
from models import News


def get_news(request):
    news_objects = News.objects.all().order_by("-updated")
    return render(request, 'index.html', {'news_objects': news_objects})

