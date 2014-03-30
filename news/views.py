from django.shortcuts import render_to_response
from news.models import News
# Create your views here.

def news(request):
    Allnews = News.objects.all()
    return render_to_response('news/shownews.html', {'Allnews':Allnews})