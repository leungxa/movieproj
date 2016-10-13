import os
import json
import requests

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader

API_KEY = os.environ['TMDB_API_KEY']

def index(request):
    template = loader.get_template('movies/index.html')
    return HttpResponse(template.render({}, request))

def send_tmdb_request(path, params=None):
    url = 'https://api.themoviedb.org/3/{}'.format(path)
    payload = {'api_key': API_KEY}
    if params:
        payload.update(params)
    headers = {'content-type': 'application/json'}

    response = requests.get(url, params=payload, headers=headers)
    print response.url
    return response

def tmdb_popular():
    path = 'movie/popular'
    response = send_tmdb_request(path)
    return json.loads(response.text)

def popular(request):
    data = tmdb_popular()
    return JsonResponse(data)

def tmdb_search(query, page=1):
    path = 'search/movie'
    params = {
        'query': query,
        'page': page,
    }

    response = send_tmdb_request(path, params)
    return json.loads(response.text)

def search(request):
    query = request.GET.get('query', '')
    page = request.GET.get('page', 1)
    print "searching for ", query
    query_data = tmdb_search(query, page)
    data = {
        'query': query,
        'query_data': query_data
    }
    response = JsonResponse(data)
    return response

def tmdb_movie_info(movie_id):
    path = 'movie/' + movie_id

    response = send_tmdb_request(path)
    return json.loads(response.text)

def movie_info(request, movie_id):
    data = tmdb_movie_info(movie_id) 
    return JsonResponse(data)