from __future__ import absolute_import

import google.appengine.ext.deferred.deferred as gae_deferred

import handlers

application = handlers.django_setup_teardown(gae_deferred.application)
