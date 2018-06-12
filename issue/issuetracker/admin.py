# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


# coding: utf-8
from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('closed', 'title', 'text', 'created', 'user')
    list_filter = ['created', 'closed']
    search_fields = ['title', 'text']

admin.site.register(Ticket, TicketAdmin)
