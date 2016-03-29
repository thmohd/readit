from django.contrib import admin
from .models import Book, Author

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Book Details",{"fields":["title","author"]}),
        ("Book Review",{"fields":["is_favourite", "review", "date_review"]})
    ]

    readonly_fields = ("date_review",)

    def book_authors(self, obj):
        return obj.list_authors()

    book_authors.short_description = "Author(s)"

    list_display = ("title","book_authors","date_review","is_favourite",)
    list_editable = ("is_favourite",)
    list_display_links = ("title","date_review",)
    list_filter = ("is_favourite",)
    search_fields = ("title","author__name")




#admin.site.register(Book, BookAdmin)
admin.site.register(Author)

