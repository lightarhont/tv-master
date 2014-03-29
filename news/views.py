from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

# Create your views here.

def news(request):
    t = get_template('frontend.html')
    result = t.render(Context())
    return HttpResponse(result)