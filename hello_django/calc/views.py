from django.http import HttpResponse
from django.views.generic.base import View
from django.shortcuts import render

# Create your views here.
def index(request, **kwargs):
    kwargs['sum'] = kwargs['a'] + kwargs['b']
    return render(request, 'calc/calc.html', kwargs)


class CalcPage(View):

    def get(self, *args, **kwargs):
        return HttpResponse('calc')