from django.shortcuts import render_to_response


def index(request):
    return render_to_response('app/index.html', {
        "title": "Образование"
    })



    # first_name = models.CharField(max_length=50)
    # middle_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # date_of_birthday = models.DateField()
    # citizenship = models.CharField(max_length=50)
    # passport_num = models.CharField(max_length=50)
    # personal_id = models.CharField(max_length=50)
    # passport_exp_date = models.DateField()
    # photo_link = models.ImageField()
    # creation_date = models.DateField(auto_now=True)
    # last_update_date = models.DateField()
    # sex = models.CharField(
    #     max_length=1,
    #     choices=SEX,
    #     default=FEMALE,
    # )

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
        "education_options": education_options
    })


def campagin_status(request):
    return render_to_response('app/campagin_status.html', {
        "title": "Статус приёмной кампании"
    })