from django.shortcuts import render_to_response


def index(request):
    return render_to_response('index.html', {
        "title": "Образование"
    })


def new_application(request):
    fields = [
        "Гражданство",
    "Номер паспорта",

    "Личный номер",
    "Дата выдачи",
    "Фотография"]
    return render_to_response('application_form.html', {
        "title": "Подача заявления",
        "fields": fields
    })


def campagin_status(request):
    return render_to_response('campagin_status.html', {
        "title": "Статус приёмной кампании"
    })