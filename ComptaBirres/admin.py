from django.contrib import admin
from ComptaBirres.models import *

@admin.register(Birra)
class BirraAdmin(admin.ModelAdmin):
    list_filter = []
    list_display = ["tirador", "timestamp", "edicio"]
    search_field = ["edicio", "tirador"]

@admin.register(Edicio)
class EdicioAdmin(admin.ModelAdmin):
    list_filter = []
    list_display = ["edicio", "totalBirres"]
    search_field = []

@admin.register(Tirador)
class EdicioAdmin(admin.ModelAdmin):
    list_filter = []
    list_display = ["name", "totalBirresTirador", "ip"]
    search_field = ["name"]
