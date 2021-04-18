# Flask サンプルアプリ

## Installation

https://flask.palletsprojects.com/en/1.1.x/installation/#installation

```
$ python --version
Python 3.8.3
$ python -m venv venv
$ . venv/bin/activate
$ pip install --upgrade pip
$ pip install Flask
$ pip install gunicorn
```

## To run the application

```
$ . venv/bin/activate
$ gunicorn sample.hello:app
 * Running on http://127.0.0.1:8000
```

## Deploy to Heroku

```
$ pip freeze > requirements.txt
$ vi Procfile
web: gunicorn training.hello:app --log-file -
$ heroku create
$ git push heroku main
```
