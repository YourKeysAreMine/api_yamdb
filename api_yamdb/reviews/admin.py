from django.contrib import admin
from .models import Category, Genre, Title, Genre_Title, Review, Comment


class GenreInline(admin.TabularInline):
    model = Title.genre.through


class TitleAdmin(admin.ModelAdmin):
    inlines = (GenreInline,)


admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Title, TitleAdmin)
admin.site.register(Genre_Title)
admin.site.register(Review)
admin.site.register(Comment)
