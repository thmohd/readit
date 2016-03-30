from django.shortcuts import render
from .models import Book

# Create your views here.

def list_books(request):
    books = Book.objects.exclude(date_review__isnull = True).prefetch_related("author")

    context = {
        "books":books,
    }
    return render(request, 'list.html', context)
