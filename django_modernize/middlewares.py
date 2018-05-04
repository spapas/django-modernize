import time

import django.conf
import django.core.exceptions


class SleepMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # time.sleep(.5)
        response = self.get_response(request)
        return response
