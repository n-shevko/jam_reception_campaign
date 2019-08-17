from django.shortcuts import render_to_response
from django.http import HttpResponse

def index(request):
    return render_to_response('index.html', {})


def new_application(request):
    d = 34
    return render_to_response('application_form.html', {})