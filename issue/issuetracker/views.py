# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


from django.views.generic import ListView
from .models import Ticket

class IssuesListView(ListView):
    model = Ticket
    template_name = 'list.html'




class IssueDetailView(DetailView):
    model = Ticket
    template_name = 'detail.html'
    
    


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('index')


class IssueCreateView(CreateView):
    model = Ticket
    template_name = 'add.html'
    fields = ['title', 'text']
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(IssueCreateView, self).form_valid(form)
