# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.


# coding: utf-8
from django.contrib import admin
from .models import *

class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'closed','text', 'created', 'solver', 'submitter', 'get_category')
    list_filter = ['created', 'closed']
    search_fields = ['title', 'text']
    
    def save_model(self, request, obj, form, change):
        if obj.closed:
            obj.solver = request.user
        else:
            obj.submitter = request.user
        super(TicketAdmin, self).save_model(request, obj, form, change)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    
    

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Category, CategoryAdmin)

