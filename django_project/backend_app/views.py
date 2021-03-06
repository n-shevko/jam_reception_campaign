from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView

from django_tables2.views import SingleTableView


from app.models import Applications
from .tables import ApplicationsTable
from .forms import ApplicationEditForm


class BackendIndex(TemplateView):
    template_name = 'backend_app/index.html'


class ApplicationsView(SingleTableView):
    model = Applications
    table_class = ApplicationsTable
    template_name = 'backend_app/applications_list.html'
    ordering = 'application_id'

    def get_queryset(self):
        return Applications.objects.filter(spec__colledge=self.request.user.employee.college).order_by('application_id')


class ApplicationEditView(UpdateView):
    model = Applications
    form_class = ApplicationEditForm
    template_name = 'backend_app/application_edit_form.html'
    success_url = reverse_lazy('backend_app:app_list')


def update_application_status(request):
    applications_ids = Applications.objects.filter(status='In Progress').values_list('application_id', flat=True)[:5]
    Applications.objects.filter(application_id__in=applications_ids).update(status='Approved')
    return redirect('backend_app:app_list')


