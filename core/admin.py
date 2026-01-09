import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import Unidade, Sala, Status, Bem, Categoria

@admin.register(Unidade)
class UnidadeAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "endereco")
    search_fields = ("nome",)


@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "unidade")
    list_filter = ("unidade",)


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")


@admin.register(Bem)
class BemAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "tombo", "unidade", "sala", "status", "categoria")
    search_fields = ("nome", "tombo")
    list_filter = ("unidade", "sala", "status", "categoria")

    def export_to_csv(self, request, queryset):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="bens.csv"'

        writer = csv.writer(response)
        writer.writerow(["ID","Nome","Tombo","Unidade","Sala","Status","Categoria" ])
        
        for bem in queryset:
            writer.writerow([bem.id,bem.nome,bem.tombo,bem.unidade,bem.sala,bem.status,
                             bem.categoria])
           

        return response

    export_to_csv.short_description = "Exportar para CSV"
    actions = ["export_to_csv"]


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id", "nome")
    search_fields = ("nome",)