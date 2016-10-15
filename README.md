# movieproj
Movie project utilizing TheMovieDB API

# Set up instructions
Install Django via pip (project requires ver 1.10)

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
mkdir ~/virtualenvdir
cd ~/virtualenvdir
virtualenv newenv
source newenv/bin/activate
```
Install django inside virtual environment
Set up and verify django installation
```
sudo pip install django
django-admin --version
```

Set up a virtualenvironment
```
pip install -r requirements
```

Ready to launch server
```
python manage.py runserver 0.0.0.0:8000
```

Homepage is located at localhost:8000/movies/
