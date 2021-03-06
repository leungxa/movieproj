# movieproj
Movie project utilizing TheMovieDB API

# Set up instructions
### Install Django via pip (project requires ver 1.10)
Install pip and virtualenv
```
(for ubuntu)
sudo apt-get update
sudo apt-get install python-pip

(for osx via homebrew)
brew update
brew install pip

sudo pip install virtualenv
```
Create virtual environment inside project directory
```
mkdir ~/projectdir
cd ~/projectdir
virtualenv newenv
source newenv/bin/activate
```
Install django inside virtual environment

Set up and verify django installation
```
sudo pip install django
django-admin --version
```

Install requirements for django project (from project directory)
```
pip install -r requirements.txt
```

### Set API key from themoviedb as environment variable

Add line `export TMDB_API_KEY=(API key goes here)` to `~/.bash_profile`, then update:
```
source ~/.bash_profile
```

### Ready to launch server
```
python manage.py runserver 0.0.0.0:8000
```

Homepage is located at localhost:8000/movies/
