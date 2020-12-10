from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import PeliculaFavorita

# Register your models here.


@admin.register(PeliculaFavorita)
class PeliculaFavoritaAdmin(ImportExportModelAdmin):
    pass