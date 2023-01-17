from django.contrib import admin
from .models import Category, Genre, Title, Genre_Title, Review, Comment


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug',)
    list_editable = ('name', 'slug',)
    search_fields = ('name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'review_id',
                    'text,author',
                    'pub_date',)
    list_editable = ('review_id', 'text,author',)
    search_fields = ('text,author',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'name',
                    'slug',)
    list_editable = ('name', 'slug',)
    search_fields = ('name',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'title_id',
                    'text',
                    'author',
                    'score',
                    'pub_date',)
    list_editable = ('title_id',
                     'text',
                     'score')
    search_fields = ('title_id',
                     'text',)


class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'name',
                    'year',
                    'category',)
    list_editable = ('name',
                     'year',)
    search_fields = ('name',
                     'year',)


admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Title)
admin.site.register(Genre_Title)
admin.site.register(Review)
admin.site.register(Comment)
