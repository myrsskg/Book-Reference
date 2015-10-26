# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import *


class AbstractAdmin(admin.ModelAdmin):
    list_display = ('name', )


class BRAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'city')
    search_fields = ('name', 'phone', )
    ordering = ('name', )


admin.site.register(BR, BRAdmin)
admin.site.register(City, AbstractAdmin)
admin.site.register(Street, AbstractAdmin)
