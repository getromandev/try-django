from multiprocessing import context
from django.shortcuts import render

from .models import Article

def article_search_view(request):
    # print('DIR ==>', dir(request))
    # print(request.GET)
    query_dict = request.GET
    # query = query_dict.get('q')
    try:
        query = int(query_dict.get('q'))
    except:
        query = None
    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {
        'object': article_obj
    }
    return render(request, 'articles/search.html', context=context)

def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj,
    }
    return render(request, 'articles/detail.html', context=context)
