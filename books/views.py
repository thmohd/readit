from django.db.models import Count
from django.shortcuts import render
from django.views.generic import DetailView, View
from .models import Author, Book

# Create your views here.

def list_books(request):
    books = Book.objects.exclude(date_review__isnull = True).prefetch_related("author")

    context = {
        "books":books,
    }
    return render(request, 'list.html', context)



class AuthorsList(View):
    def get(self, request):
        authors = Author.objects.annotate(
            published_books = Count("books")
        ).filter(
            published_books__gt = 0
        )

        context ={
            "authors": authors,
        }

        return render(request, "authors.html",context)


class BookDetails(DetailView):
    #context_object_name = "book"
    #queryset = Book.objects.all()
    model = Book
    template_name = "book.html"

class AuthorDetails(DetailView):
    model = Author
    #context_object_name = "author"
    template_name = "author.html"


