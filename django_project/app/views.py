from django.shortcuts import render_to_response


def index(request):
    return render_to_response('index.html', {
        "title": "Образование"
    })


def new_application(request):
    return render_to_response('application_form.html', {
        "title": "Подача заявления"
    })


def campagin_status(request):
    return render_to_response('campagin_status.html', {
        "title": "Статус приёмной кампании"
    })