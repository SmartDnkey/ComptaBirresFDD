from django.contrib import admin
from ComptaBirres.models import *

@admin.register(Birra)
class BirraAdmin(admin.ModelAdmin):
    list_display = ["tirador", "timestamp"]


@admin.register(Edicio)
class EdicioAdmin(admin.ModelAdmin):

    list_display = ["edicio", "totalBirres", "dataString"]
    readonly_fields = ('dataString',)

@admin.register(Tirador)
class EdicioAdmin(admin.ModelAdmin):

    list_display = ["name", "totalBirresTirador", "ip", "edicio"]