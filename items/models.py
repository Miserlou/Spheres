from django.db import models
from django.forms import ModelForm
from django.template.defaultfilters import slugify

from datetime import datetime

class Item(models.Model):
    url = models.CharField(max_length=200)
    thumb_url = models.CharField(max_length=200)
    date = models.DateTimeField('date', blank=True, default=datetime.now)

    def __unicode__(self):
        return self.title

class ItemForm(ModelForm):
    class Meta:
        model = Item
        exclude = ('date',)