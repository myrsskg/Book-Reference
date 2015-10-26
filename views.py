# -*- coding: utf-8 -*-
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, View, DetailView
from django.http import HttpResponse, Http404
from .forms import *
from .models import *

import urllib
from django.core.urlresolvers import reverse


class VBRs(ListView):
    template_name = 'br/base.html'
    context_object_name = 'br'
    model = BR

    def get_queryset(self):
        br = self.model.objects.all()

        name = self.request.GET.get('name', None)
        if name:
            br = br.filter(name__icontains=name)

        phone = self.request.GET.get('phone', None)
        if phone:
            br = br.filter(phone__icontains=phone)

        street = self.request.GET.get('street', None)
        if street:
            br = br.filter(street__icontains=street)

        id = self.request.GET.get('id', None)
        if id:
            br = br.filter(id=id)

        return br


def build_url(*args, **kwargs):
    get = kwargs.pop('get', {})
    url = reverse(*args, **kwargs)
    if get:
        url += '?' + urllib.urlencode(get)
    return url


class VBRadd(CreateView):
    form_class = FormBR
    template_name = 'br/br_form.html'
    model = BR

    def get_success_url(self):
        return build_url('br:vbr', get={'id': self.object.id})


class VBRedit(UpdateView):
    form_class = FormBR
    template_name = 'br/br_form.html'
    model = BR

    def get_success_url(self):
        return build_url('br:vbr', get={'id': self.object.id})


class VBRdel(DeleteView):
    model = BR

    def get_success_url(self):
        return build_url('br:vbr', get={'id': self.object.id})
