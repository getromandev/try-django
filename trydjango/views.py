"""
To Render html web pages
"""
import random
from django.http import HttpResponse

from articles.models import Article
from django.template.loader import render_to_string


def home_view(request, *args, **kwargs):
    """
    Take in a request (Django sends request)
    Return HTML as a response (We pick to return the response)
    """
    
    name = 'Justin'
    random_id = random.randint(1, 4)
    
    # from the database
    article_obj = Article.objects.get(id=random_id)
    article_qs = Article.objects.all()
    
    context = {
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content,
        "object_list": article_qs,
        "object": article_obj
    }
    
    HTML_STRING = render_to_string('home-view.html', context=context)
    
    return HttpResponse(HTML_STRING)
 