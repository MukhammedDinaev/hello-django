from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView, View
from hello_django.calc import views




class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context

def index(request):
    return redirect(reverse(views.index, kwargs={'a': 45, 'b': 2}))

