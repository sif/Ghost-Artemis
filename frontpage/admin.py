"""For adding models to admininistration page for splash related things."""

from django.contrib import admin

from .models import Quotation

admin.site.register(Quotation)
