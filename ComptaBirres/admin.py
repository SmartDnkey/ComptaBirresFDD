from django.contrib import admin
from ComptaBirres.models import *

@admin.register(Birra)
class BirraAdmin(admin.ModelAdmin):
    list_filter = []
    list_display = ["tirador", "timestamp"]
    search_field = ["tirador"]

@admin.register(Edicio)
class EdicioAdmin(admin.ModelAdmin):
    list_filter = []
    list_display = ["edicio", "totalBirres", "dataString"]
    readonly_fields = ('dataString',)
    search_field = []

@admin.register(Tirador)
class EdicioAdmin(admin.ModelAdmin):
    list_filter = []
    list_display = ["name", "totalBirresTirador", "ip", "edicio"]
    search_field = ["name"]
