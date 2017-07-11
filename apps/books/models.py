from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100)
    in_print = models.BooleanField(True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "id: " + str(self.id) + ", Title: " + str(self.title) + " Author: " + str(self.author) + " Published Date: " + str(self.published_date) + ", Category: ", str(self.category)
