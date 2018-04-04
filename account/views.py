from django.views.generic import CreateView
from .forms import SignUpForm
from django.core.urlresolvers import reverse_lazy

class SignUp(CreateView):

    form_class = SignUpForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('login')