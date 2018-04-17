from __future__ import unicode_literals
from django.db import models
from django import forms
from django.urls import reverse

class Data(models.Model):
    user = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    file = models.FileField()

    def get_absolute_url(self):
        return reverse('upload:detail')

    def __str__(self):
        return self.user
