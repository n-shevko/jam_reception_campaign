import django_tables2 as tables
from django.utils.safestring import mark_safe

from app.models import Applications


class ApplicationsTable(tables.Table):

    def render_application_id(self, value):
        return mark_safe(f'<a href="/back/app_edit/{value}">{value}</a>')

    class Meta:
        model = Applications
        template_name = 'django_tables2/bootstrap.html'
        row_attrs = {
            'data-id': lambda record: record.pk
        }
