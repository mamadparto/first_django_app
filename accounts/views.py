from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "registration\signup.html"
    success_url = reverse_lazy('list_of_post')
