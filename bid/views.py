from django.views.generic import CreateView, ListView, UpdateView
from django.core.urlresolvers import reverse_lazy

from django.contrib import messages

from .forms import AddBidForm
from .models import *
from document.models import Document


class MyBids(ListView):
    model = Bid
    template_name = 'bid/my_bids.html'
    context_object_name = 'bids'

    def get_queryset(self):
        queryset = Bid.objects.filter(user=self.request.user).order_by('-created')
        return queryset


class AddBid(CreateView):
    template_name = 'bid/add_bid.html'
    form_class = AddBidForm
    success_url = reverse_lazy('bid:my-bids')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddBid, self).form_valid(form)


class EditBid(UpdateView):
    model = Bid
    fields = [
        'bid_entity',
        'bid_number',
        'bid_title',
        'bid_due',
        'bid_time',
        'bid_question',
        'bid_issue',
        'bid_contact_name',
        'bid_contact_email',
        'branch',
        'branch_region',
        'branch_contact',
        'documents',
    ]
    template_name = 'bid/edit_bid.html'

    def get_success_url(self):
        return reverse_lazy('bid:edit-bid', kwargs={'pk': self.object.pk})


class AddDocuments(ListView):
    model = Document
    template_name = 'bid/add_documents.html'
    context_object_name = 'documents'

    def get_queryset(self):
        queryset = Document.objects.filter(user=self.request.user).order_by('-created')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(AddDocuments, self).get_context_data(**kwargs)
        context['bid'] = Bid.objects.get(pk=self.kwargs.get('pk'))
        return context

    def post(self, request, *args, **kwargs):
        if request.POST.get('add'):
            bid = Bid.objects.get(pk=self.kwargs.get('pk'))
            document = Document.objects.get(pk=request.POST.get('add'))
            bid.documents.add(document)

        if request.POST.get('remove'):
            bid = Bid.objects.get(pk=self.kwargs.get('pk'))
            document = Document.objects.get(pk=request.POST.get('remove'))
            bid.documents.remove(document)

        # return super(AddDocuments, self).post(request, *args, **kwargs)
        return self.get(self, *args, **kwargs)
