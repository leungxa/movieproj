from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader

from movies.view_helpers import popular_movies_context, search_results_context, \
    movie_info_context

def index(request):
    context = popular_movies_context()
    template = loader.get_template('movies/index.html')
    return HttpResponse(template.render(context, request))


def search(request):
    query = request.GET.get('query', '')
    if not query:
        return HttpResponseRedirect(reverse('index'))
    page = request.GET.get('page', 1)
    context = search_results_context(query, page)

    template = loader.get_template('movies/search_results.html')
    return HttpResponse(template.render(context, request))


def movie_info(request, movie_id):
    context = movie_info_context(movie_id)

    template = loader.get_template('movies/details.html')
    return HttpResponse(template.render(context, request))