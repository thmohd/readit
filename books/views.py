from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, View
from .models import Author, Book
from .forms import ReviewForm


# Create your views here.

def list_books(request):
    books = Book.objects.exclude(date_review__isnull=True).prefetch_related("author")

    context = {
        "books": books,
    }
    return render(request, 'list.html', context)


class AuthorsList(View):
    def get(self, request):
        authors = Author.objects.annotate(
            published_books=Count("books")
        ).filter(
            published_books__gt=0
        )

        context = {
            "authors": authors,
        }

        return render(request, "authors.html", context)


class BookDetails(DetailView):
    # context_object_name = "book"
    # queryset = Book.objects.all()
    model = Book
    template_name = "book.html"


class AuthorDetails(DetailView):
    model = Author
    # context_object_name = "author"
    template_name = "author.html"


def review_books(request):
    """
    List all of the books that we want to review.
    """
    books = Book.objects.filter(date_review__isnull=True).prefetch_related('author')

    context = {
        'books': books,
    }

    return render(request, "list-to-review.html", context)


def review_book(request, pk):
    """
    Review an individual book
    """
    book = get_object_or_404(Book, pk=pk)
    form = ReviewForm

    context = {
        'book': book,
        'form': form
    }

    return render(request, "review-book.html", context)
