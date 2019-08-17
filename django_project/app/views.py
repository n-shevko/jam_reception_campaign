from django.shortcuts import render_to_response


def index(request):
    return render_to_response('app/index.html', {
        "title": "Образование"
    })


def new_application(request):
    education_options = {
        "Minsk": {
            "BGU": ["Povar", "Kuharka"],
            "BGUIR": ["Koder"]
        },
        "Gomel": {
            "BELGUT": ['Sviaz'],
            "GTEK": ["Proger"]
        }
    }
    return render_to_response('app/application_form.html', {
        "title": "Подача заявления",
        "fields": [
            ['Гражданство', 'citizenship'],
            ['Номер паспорта', 'passport_num'],
            ['Личный номер', 'personal_id'],
            ['Дата выдачи', 'passport_exp_date'],
            ['Фотография', 'photo']
        ],
        "subjects": [['Математика', 'Русский язык'], ['Английский язык', 'Изо']],
        "tests": ["Математика", "Русский"],
        "education_options": education_options,
        "cheaters": [
            "Победитель олимпиады",
            "Сирота",
            "Спортсмены"
        ]
    })


def campagin_status(request):
    return render_to_response('app/campagin_status.html', {
        "title": "Статус приёмной кампании"
    })