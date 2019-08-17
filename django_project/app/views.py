from django.shortcuts import render_to_response


def index(request):
    return render_to_response('app/index.html', {
        "title": "Образование"
    })


def new_application(request):
    return render_to_response('app/application_form.html', {
        "title": "Подача заявления",
        "fields": [
            'Гражданство',
            'Номер паспорта',
            'Личный номер',
            'Дата выдачи',
            'Фотография'
        ],
        "subjects": [['Математика', 'Русский язык'], ['Английский язык', 'Изо']],
        "tests": ["Математика", "Русский"]
    })


def campagin_status(request):
    return render_to_response('app/campagin_status.html', {
        "title": "Статус приёмной кампании"
    })