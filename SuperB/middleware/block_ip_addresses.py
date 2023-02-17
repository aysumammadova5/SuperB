from django.utils.deprecation import MiddlewareMixin
from django.core.exceptions import PermissionDenied

class BlackListIPAddressMiddleware(MiddlewareMixin):
    BLACK_LIST = [
        # '192.168.155.138'
    ]

    def process_request(self, request):
        if request.META.get('REMOTE_ADDR') in self.BLACK_LIST:
            raise PermissionDenied
