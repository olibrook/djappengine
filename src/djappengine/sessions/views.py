from datetime import datetime

from djappengine.sessions.mapper import DeleteMapper
from djappengine.sessions.models import Session

from django.http import HttpResponse
from django.views.generic.base import View


class SessionCleanUpCron(View):
    """
    View used by cron to clear sessions that have expired
    """
    def get(self, request, *args, **kwargs):
        mapper = DeleteMapper(
            Session,
            filters={
                'lt': ('expire_date', datetime.utcnow())
            }
        )
        mapper.start()
        return HttpResponse('Session cleaner mapper started')

session_clean_up = SessionCleanUpCron.as_view()
