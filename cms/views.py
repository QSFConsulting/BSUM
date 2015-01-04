from django.shortcuts import render
from models import News


def get_index(request):
    news_objects = News.objects.all().order_by("-updated")[:2]
    for new in news_objects:
        new.cut = False
        if len(new.content):
            tmp_content = new.content[:360]
            tmp_content = " ".join(tmp_content.split(" ")[:-1]) + "..."
            new.content = tmp_content
            new.cut = True
        if new.override_date:
            new.updated = new.override_date
    news_objects = sorted(
        list(news_objects),
        key=lambda x: x.updated,
        reverse=True)
    return render(request, 'index.html', {'news_objects': news_objects})


def get_news(request):
    news_objects = News.objects.all().order_by("-updated")
    for new in news_objects:
        if new.override_date:
            new.updated = new.override_date
    news_objects = sorted(
        list(news_objects),
        key=lambda x: x.updated,
        reverse=True)
    return render(request, 'news.html', {'news_objects': news_objects})
