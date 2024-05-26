from django.contrib import admin

from .models import Book, Author, Address, Country

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    # Fields that are only 'read only' inside a tuple:
    # readonly_fields = ("slug",)
    # Populate a field:
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating")
    list_display = ("title", "author")


# class AuthorAdmin(admin.ModelAdmin):
#     list_filter = ("first_name", "last_name")
#     list_display = ("first_name", "last_name")


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)
