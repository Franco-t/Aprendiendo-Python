from django.contrib.sessions.models import Session
from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import logout
import logging

logger = logging.getLogger(__name__)

class SingleSessionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_authenticated:
            current_session_key = request.session.session_key
            user_sessions = Session.objects.filter(expire_date__gte=timezone.now())
            for session in user_sessions:
                data = session.get_decoded()
                if data.get('_auth_user_id') == str(request.user.id) and session.session_key != current_session_key:
                    logger.debug(f"Closing session {session.session_key} for user {request.user.id}")
                    session.delete()
                    if session.session_key == current_session_key:
                        logout(request)
                    break