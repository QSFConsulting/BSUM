from django.shortcuts import render
from models import News


def get_index(request):
    number_of_news = 3
    content_cut = 360

    news_objects = News.objects.all().order_by("-updated")
    for new in news_objects:
        new.cut = False
        if len(new.content) > content_cut:
            tmp_content = new.content[:content_cut]
            tmp_content = " ".join(tmp_content.split(" ")[:-1]) + "..."
            new.content = tmp_content
            new.cut = True
        if new.override_date:
            new.updated = new.override_date
    news_objects = sorted(
        list(news_objects),
        key=lambda x: x.updated,
        reverse=True)[:number_of_news]
    return render(request, 'index.html', {'news_objects': news_objects})


def get_references(request):
    return render(request, 'references.html')


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
