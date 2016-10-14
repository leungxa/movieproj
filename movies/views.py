import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

from movies.tmdb_utils import send_tmdb_request, tmdb_popular, tmdb_search, \
    tmdb_movie_info, get_tmdb_poster_url, get_tmdb_backdrop_url

def index(request):
    context = {}
    popular_movies = tmdb_popular()
    top_movies = []
    for i in range(10):
        if i < len(popular_movies['results']):
            movie_data = popular_movies['results'][i]
            top_movies.append({
                'id': movie_data['id'],
                'title': movie_data['title'],
                'poster_image': get_tmdb_poster_url(movie_data['poster_path']) or "",
                'details_url': '/movies/{}/'.format(movie_data['id'])
            })
    context['movies'] = top_movies
    template = loader.get_template('movies/index.html')
    return HttpResponse(template.render(context, request))


def search(request):
    query = request.GET.get('query', '')
    if not query:
        return HttpResponseRedirect(reverse('index'))
    page = request.GET.get('page', 1)
    query_data = tmdb_search(query, page)
    results = []
    for i in range(len(query_data['results'])):
        movie = query_data['results'][i]
        release_year = 'Unspecified'
        if movie['release_date']:
            dt = datetime.datetime.strptime(movie['release_date'], '%Y-%m-%d')
            release_year = dt.year
        results.append({
            'id': movie['id'],
            'title': movie['title'],
            'poster_image': get_tmdb_poster_url(movie['poster_path']) or "",
            'year': release_year,
            'details_url': '/movies/{}/'.format(movie['id'])
        })
    context = {
        'query': query,
        'total_results': query_data['total_results'],
        'total_pages': query_data['total_pages'],
        'page': query_data['page'],
        'results': results,
    }

    template = loader.get_template('movies/search_results.html')
    return HttpResponse(template.render(context, request))


def movie_info(request, movie_id):
    context = {}
    movie_data = tmdb_movie_info(movie_id)
    release_date = 'Unknown Release Date'
    release_year = 'Unspecified'
    imdb_url = ''
    if 'imdb_id' in movie_data:
        imdb_url = 'http://www.imdb.com/title/{}/'.format(movie_data['imdb_id'])
    if 'release_date' in movie_data:
        dt = datetime.datetime.strptime(movie_data['release_date'], '%Y-%m-%d')
        release_year = dt.year
        release_date = dt.strftime('%B %-d, %Y')
    context['movie'] = {
        'id': movie_data['id'],
        'title': movie_data['title'],
        'poster_image': get_tmdb_poster_url(movie_data['poster_path']) or '',
        'backdrop_image': get_tmdb_backdrop_url(movie_data['backdrop_path']) or '',
        'year': release_year,
        'release_date': release_date,
        'overview': movie_data['overview'],
        'revenue': movie_data['revenue'],
        'budget': movie_data['budget'],
        'vote_avg': movie_data['vote_average'],
        'genres': movie_data['genres'],
        'runtime': movie_data['runtime'],
        'status': movie_data['status'],
        'languages': movie_data['spoken_languages'],
        'production_companies': movie_data['production_companies'],
        'production_countries': movie_data['production_countries'],
        'imdb_url': imdb_url,
    }
    template = loader.get_template('movies/details.html')
    return HttpResponse(template.render(context, request))