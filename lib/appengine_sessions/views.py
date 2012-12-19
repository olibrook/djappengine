from appengine_sessions.backends.db import SessionStore
from appengine_sessions.mapper import DeleteMapper
from appengine_sessions.models import Session
from datetime import datetime
from django.contrib.sessions.backends.base import SessionBase
from django.http import HttpResponse
from django.views.generic.base import View



class SessionCleanUpCron(View):
    """
        View used by cron to clear sessions that have expired
    """
    
    def get(self, request, *args, **kwargs):
        
        mapper = DeleteMapper(Session,filters={'lt': ('expire_date', datetime.utcnow())})
        mapper.start()
        
        return HttpResponse('Session cleaner mapper started')
    
    
    
class GenerateSession(View):
    
    def get(self, request, *args, **kwargs):
        ss = SessionStore()
        for i in range(0,100):
            session = Session(session_key=ss._get_new_session_key(),expire_date=datetime.utcnow())
        