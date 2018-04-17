from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy

from .forms import BidForm

class Bid(FormView):
    template_name = 'bid/bid.html'
    form_class = BidForm
    success_url = reverse_lazy('webpages:home')

    def form_valid(self, form):
        form.save()
        return super(Bid, self).form_valid(form)