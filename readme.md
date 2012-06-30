#djappengine

A lightweight integration focussed on the strengths of django and App Engine.

## What’s in the box?

### app.yaml

- Set’s up static resources
- Points all other paths to the WSGI app


### main.py

- Sets up env variables and the path
- Determines if we're running locally
- Routes logging for production
- Defines the WSGI app


### manage.py

- Friendly reminder not to use runserver
- Sorts out paths using dev_appserver

### settings.py

- Sets up caching
- Sets up sessions

### urls.py

- Just points to core’s url config

### lib/memcache

- So App Engine's memcache is seen by django

### core

- A simple example app to get you started


## What's missing

- A little more fiddling (nearly there)
- Docs on deploying a 'hello world!', remote shell and testing
- CloudSQL configuration and docs

[Track progress here](https://github.com/potatolondon/djappengine/issues/milestones), we are on it.