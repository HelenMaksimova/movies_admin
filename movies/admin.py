from django.contrib import admin

from .models import FilmWork, Genre, GenreFilmWork, Person, PersonFilmWork


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ("full_name",)


class GenreFilmWorkInline(admin.TabularInline):
    model = GenreFilmWork
    extra = 1


class PersonFilmWorkInline(admin.TabularInline):
    model = PersonFilmWork
    extra = 1


@admin.register(FilmWork)
class FilmWorkAdmin(admin.ModelAdmin):
    inlines = (GenreFilmWorkInline, PersonFilmWorkInline)
    list_display = ("title", "type", "creation_date", "rating", "id")
    list_filter = ("type", "rating")
    search_fields = ("title", "description")
    ordering = ["title"]
    list_per_page = 50
