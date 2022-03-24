from django.http import HttpResponse
from django.views.generic.base import View

# Create your views here.
def index(request, **kwargs):
    return HttpResponse(str(kwargs['a']) + ' + ' + str(kwargs['b']) + ' = ' + str(kwargs['a'] + kwargs['b']))


class CalcPage(View):

    def get(self, *args, **kwargs):
        return HttpResponse('calc')