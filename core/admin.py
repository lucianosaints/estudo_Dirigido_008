from django.contrib import admin

from .models import Unidade,Sala,Status,Bem

@admin.register(Unidade)

class UnidadeAdmin(admin.ModelAdmin):
    list_display = ("id","nome","enedereco")
    search_fields = ("nome",)

@admin.register(Sala)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = ("id")



# Register your models here.
