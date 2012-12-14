from google.appengine.ext import ndb


class Session(ndb.Model):
    session_key = ndb.StringProperty()
    session_data = ndb.TextProperty()
    expire_date = ndb.DateTimeProperty()

    def get_decoded(self):
        return SessionStore().decode(self.session_data)


# At the bottom to win against circular imports
from appengine_sessions.backends.db import SessionStore
