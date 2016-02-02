from django.core.urlresolvers import reverse
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext

import json

from .models import Item, ItemForm

def upload(request):

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save()
            return HttpResponseRedirect(reverse('view_item', kwargs={'item_id': item.pk}))

    items = Item.objects.all().order_by('-pk')[:50]
    form = ItemForm()

    return render_to_response('upload.html', {'items': items, 'form': form}, context_instance=RequestContext(request))

def view_item(request, item_id):

    item = Item.objects.get(pk=item_id)
    return render_to_response('view_item.html', {'item': item}, context_instance=RequestContext(request))