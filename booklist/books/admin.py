from django.contrib import admin
from .models import Book

# Register your models here.
admin.site.register(Book)

class BookListAdmin(admin.ModelAdmin):
    list_display = ('title','author','date_published','number_pages','type_book')
    list_filter = ('title','author','date_published','type_book')
    search_field = ('title','author')
    date_hierarchy ='date_published'
    ordering=['title','author','date_published','type_book']

    
