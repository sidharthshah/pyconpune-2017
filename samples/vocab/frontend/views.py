from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Word

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['word_list'] = Word.objects.all()
        return context
