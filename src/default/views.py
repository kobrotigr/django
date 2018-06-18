from django.views.generic import View
from django.http import HttpResponse
from django.conf import settings

# Create your views here.
class Main(View):
    def get(self, request, *args):
        return HttpResponse('Hello, {}'.format(settings.HELLO_NAME))