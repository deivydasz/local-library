from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Language, Book, BookInstance

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(BookInstance)

