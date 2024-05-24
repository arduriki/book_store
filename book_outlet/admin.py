from django.contrib import admin

from .models import Book

# Register your models here.


class BookAdmin(admin.ModelAdmin):
    # Fields that are only 'read only' inside a tuple:
    # readonly_fields = ("slug",)
    # Populate a field:
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating")
    list_display = ("title", "author")


admin.site.register(Book, BookAdmin)
