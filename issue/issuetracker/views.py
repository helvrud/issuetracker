# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, CreateView, ListView

from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime, timedelta
import pytz
# Create your views here.
from .models import Ticket


def index(request):
    # Some statistics 
    tickets = model.objects.all()
    total_lifetime = timedelta(microseconds=-1)
    number_of_solved_issues = 0
    number_of_unsolved_issues = 0
    lifetimes = []
    for t in tickets:
        if t.closeddate:
            number_of_solved_issues +=1
            
            lifetimes.append(t.closeddate - t.created)
            
        else:
            number_of_unsolved_issues +=1
            lifetimes.append(pytz.utc.localize(datetime.now()) - t.created)
            
    longest_time = max(lifetimes)
    shortest_time = min(lifetimes)
    for lt in lifetimes: total_lifetime+=lt
    average_lifetime = lt / (number_of_solved_issues+number_of_unsolved_issues)
    
    
    
    #~ latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #~ template = loader.get_template('list.html')
    context = {
        'average_lifetime': average_lifetime,
        'longest_time': longest_time,
        'shortest_time': shortest_time,
    }
    #~ return HttpResponse(template.render(context, request))   
    return render(request, 'list.html', context)
    
    
    
    
class IssuesListView(ListView):
    model = Ticket
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        context = super(IssuesListView, self).get_context_data(**kwargs)
        
        # Some statistics 
        tickets = Ticket.objects.all()
        total_lifetime = timedelta(microseconds=-1)
        number_of_solved_issues = 0
        number_of_unsolved_issues = 0
        lifetimes = []
        for t in tickets:
            if t.closeddate:
                number_of_solved_issues +=1
                
                lifetimes.append(t.closeddate - t.created)
                
            else:
                number_of_unsolved_issues +=1
                lifetimes.append(pytz.utc.localize(datetime.now()) - t.created)
                
        longest_time = max(lifetimes)
        shortest_time = min(lifetimes)
        for lt in lifetimes: total_lifetime+=lt
        average_lifetime = lt / (number_of_solved_issues+number_of_unsolved_issues)
        
        
        
        #~ latest_question_list = Question.objects.order_by('-pub_date')[:5]
        #~ template = loader.get_template('list.html')
        context['average_lifetime'] = average_lifetime
        context['longest_time'] = longest_time
        context['shortest_time'] = shortest_time
        
        context['now'] = datetime.now()
        return context


#~ class IssueDetailView(DetailView):
class IssueDetailView(UpdateView):
    model = Ticket
    template_name = 'detail.html'
    fields = ['closed']
    success_url = reverse_lazy('index')
    def form_valid(self, form):
        if form.instance.closed:
            form.instance.solver = self.request.user
            form.instance.closeddate = datetime.now()
        else:
            form.instance.solver = None
            form.instance.closeddate = None
        return super(IssueDetailView, self).form_valid(form)





class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('index')


class IssueCreateView(CreateView):
    model = Ticket
    template_name = 'add.html'
    fields = ['title', 'text', 'category']

    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.submitter = self.request.user
        return super(IssueCreateView, self).form_valid(form)



