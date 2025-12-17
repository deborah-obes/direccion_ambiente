from django.shortcuts import render
from .forms import ContactoForm
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.


class ContactoUsuario(CreateView):
    template_name = 'contacto/contacto.html'
    form_class = ContactoForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        messages.success(self.request, 'Consulta enviada.')
        return super().form_valid(form)

    