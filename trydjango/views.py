"""
To Render html web pages
"""
import random
from django.http import HttpResponse

from articles.models import Article
from django.template.loader import render_to_string


def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    
    article_obj = Article.objects.get(id=1)
    article_qs = Article.objects.all()
    
    context = {
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content,
        "object_list": article_qs
    }
    
    HTML_STRING = render_to_string('home-view.html', context=context)
    
    return HttpResponse(HTML_STRING)
 