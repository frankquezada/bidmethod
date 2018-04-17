from django.views.generic import CreateView, ListView, UpdateView
from django.urls import reverse_lazy

from .models import *

class MyDocuments(ListView):
    model = Document
    template_name = 'document/my_documents.html'
    context_object_name = 'documents'

    def get_queryset(self):
        queryset = Document.objects.filter(user = self.request.user).order_by('-created')
        return queryset

class AddDocument(CreateView):
    model = Document
    fields = ['title', 'file']
    template_name = 'document/add_document.html'
    success_url = reverse_lazy('document:my-documents')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddDocument, self).form_valid(form)

class EditDocument(UpdateView):
    model = Document
    fields = ['title', 'file']
    template_name = 'document/edit_document.html'

    def get_success_url(self):
        return reverse_lazy('document:edit-document', kwargs = {'pk': self.object.pk})