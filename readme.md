##A streamlined Django and App Engine integration.

Run locally:

    git clone git@github.com:potatolondon/djappengine.git
    cd djappengine
    dev_appserver .

Visit <http://localhost:8000> to marvel at your work.

Now deploy to appspot, first set up an app on <http://appengine.google.com> and replace `application` in `app.yaml` with the name of your app (in your text editor or like this):

    sed -i '' 's/djappeng1ne/myappid/' app.yaml

You're ready to deploy:

    appcfg.py update .

The Django app in `core` is there to get you started. Have fun!

## So what's going on?

### app.yaml

- Sets up static resources
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