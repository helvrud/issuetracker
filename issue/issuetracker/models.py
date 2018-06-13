# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


# coding: utf-8
from django.db import models
from django.contrib.auth.models import User





class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        
class Ticket(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    closeddate = models.DateTimeField(null=True, blank=True, verbose_name=u'Closed date', auto_now_add=False)
    submitter = models.ForeignKey(User, related_name='Submitter', blank=True, null=True)
    
    solver = models.ForeignKey(User, default=None, blank=True, related_name='Solver', null=True)
    
    def __unicode__(self):
        return self.title
    class Meta:
        ordering = ('title',)




    category      = models.ManyToManyField(Category, default=None, blank=True, verbose_name=u'Category')
    
    def get_category(self):
        return ",".join([str(p) for p in self.category.all()])

    #~ def __unicode__(self):
        #~ return "{0}".format(self.title)
