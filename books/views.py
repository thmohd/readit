from django.core.urlresolvers import reverse
from django.db.models import Count
from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import DetailView, View
from django.views.generic.edit import CreateView
from .models import Author, Book
from .forms import ReviewForm, BookForm


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


class ReviewList(View):
    """
    List all of the books that we want to review.
    """
    def get(self, request):
        books = Book.objects.filter(date_review__isnull=True).prefetch_related('author')
        form = BookForm

        context = {
            'books': books,
            'form': form,
        }

        return render(request, "list-to-review.html", context)

    def post(self, request):
        form = BookForm(request.POST)
        books = Book.objects.filter(date_review__isnull=True).prefetch_related('author')

        if form.is_valid():
            form.save()
            return redirect('review-books')

        context = {
            'books': books,
            'form': form,
        }

        return render(request, "list-to-review.html", context)

def review_book(request, pk):
    """
    Review an individual book
    """
    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":
        form = ReviewForm(request.POST)

        if form.is_valid():
            book.is_favourite = form.cleaned_data['is_favourite']
            book.review = form.cleaned_data['review']
            book.save()

            return redirect('review-books')
    else:
        form = ReviewForm

    context = {
        'book': book,
        'form': form
    }

    return render(request, "review-book.html", context)


class CreateAuthor(CreateView):
    model = Author
    fields = ['name',]
    template_name = 'create-author.html'

    def get_success_url(self):
        return reverse('review-books')
