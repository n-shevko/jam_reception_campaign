from django.shortcuts import render
from django.views.generic import TemplateView


class BackendIndex(TemplateView):
    template_name = 'backend_app/index.html'
