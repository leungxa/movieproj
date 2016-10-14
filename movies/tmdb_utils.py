import os
import json
import requests

API_KEY = os.environ['TMDB_API_KEY']

def send_tmdb_request(path, params=None):
    url = 'https://api.themoviedb.org/3/{}'.format(path)
    payload = {'api_key': API_KEY}
    if params:
        payload.update(params)
    headers = {'content-type': 'application/json'}

    response = requests.get(url, params=payload, headers=headers)
    return response

def tmdb_popular():
    path = 'movie/popular'
    response = send_tmdb_request(path)
    return json.loads(response.text)

def tmdb_search(query, page=1):
    path = 'search/movie'
    params = {
        'query': query,
        'page': page,
    }

    response = send_tmdb_request(path, params)
    return json.loads(response.text)

def tmdb_movie_info(movie_id):
    path = 'movie/' + movie_id

    response = send_tmdb_request(path)
    return json.loads(response.text)

def get_tmdb_poster_url(url):
    if url:
        return 'https://image.tmdb.org/t/p/w300/{}'.format(url)
    return None

CONFIGURATION = {
  "images": {
    "base_url": "http://image.tmdb.org/t/p/",
    "secure_base_url": "https://image.tmdb.org/t/p/",
    "backdrop_sizes": [
      "w300",
      "w780",
      "w1280",
      "original"
    ],
    "logo_sizes": [
      "w45",
      "w92",
      "w154",
      "w185",
      "w300",
      "w500",
      "original"
    ],
    "poster_sizes": [
      "w92",
      "w154",
      "w185",
      "w342",
      "w500",
      "w780",
      "original"
    ],
    "profile_sizes": [
      "w45",
      "w185",
      "h632",
      "original"
    ],
    "still_sizes": [
      "w92",
      "w185",
      "w300",
      "original"
    ]
  },
  "change_keys": [
    "adult",
    "air_date",
    "also_known_as",
    "alternative_titles",
    "biography",
    "birthday",
    "budget",
    "cast",
    "certifications",
    "character_names",
    "created_by",
    "crew",
    "deathday",
    "episode",
    "episode_number",
    "episode_run_time",
    "freebase_id",
    "freebase_mid",
    "general",
    "genres",
    "guest_stars",
    "homepage",
    "images",
    "imdb_id",
    "languages",
    "name",
    "network",
    "origin_country",
    "original_name",
    "original_title",
    "overview",
    "parts",
    "place_of_birth",
    "plot_keywords",
    "production_code",
    "production_companies",
    "production_countries",
    "releases",
    "revenue",
    "runtime",
    "season",
    "season_number",
    "season_regular",
    "spoken_languages",
    "status",
    "tagline",
    "title",
    "translations",
    "tvdb_id",
    "tvrage_id",
    "type",
    "video",
    "videos"
  ]
}