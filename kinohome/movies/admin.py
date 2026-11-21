from django.contrib import admin
from .models import Genre, Movie, Episode, Advertisement


class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "content_type", "release_year", "rating")
    list_filter = ("content_type", "genres", "release_year")
    search_fields = ("title",)
    filter_horizontal = ("genres",)
    inlines = [EpisodeInline]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ("name",)


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active")
    list_filter = ("is_active",)