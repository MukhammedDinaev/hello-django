from django.http import HttpResponse
from django.views.generic.base import View

# Create your views here.
def index(request):
    return HttpResponse('calc')


class CalcPage(View):

    def get(self, *args, **kwargs):
        return HttpResponse('calc')