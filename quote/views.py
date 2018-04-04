from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from django.urls import reverse_lazy

from .models import *

class MyFiles(ListView):
    template_name = 'quote/my_files.html'
    model = UserFile
    context_object_name = 'files'

    def get_queryset(self):
        queryset = UserFile.objects.filter(user = self.request.user).order_by('-created')
        return queryset

class AddFile(CreateView):
    fields = ['title', 'file']
    model = UserFile
    template_name = 'quote/add_file.html'
    success_url = reverse_lazy('quote:my-files')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddFile, self).form_valid(form)

class EditFile(UpdateView):
    fields = ['title', 'file']
    model = UserFile
    template_name = 'quote/edit_file.html'

    def get_success_url(self):
        return reverse_lazy('quote:edit-file', kwargs = {'pk': self.object.pk})