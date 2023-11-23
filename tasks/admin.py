from django.contrib import admin
from .models import Notas


class NotasAdmin(admin.ModelAdmin):
    readonly_fields= ("created", )

# Register your models here.
admin.site.register(Notas, NotasAdmin)
