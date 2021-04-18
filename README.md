# Flask サンプルアプリ

## Installation

https://flask.palletsprojects.com/en/1.1.x/installation/#installation

```
$ python --version
 * python3.* であることを確認してください。
 * python2.*の場合は、`python3 --version` で、python3が実行できるかもしれません。
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
$ git add .
$ git commit -m 'Deploy to Heroku.'
$ heroku login
$ heroku create
$ git push heroku main
```
