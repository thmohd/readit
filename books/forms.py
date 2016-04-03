from django import forms
from .models import Book

class ReviewForm(forms.Form):
    """
    For review A book
    """

    is_favourite = forms.BooleanField(
        label="Favourite?",
        help_text="In your top 100 books of all the time?",
        required=False,
    )

    review = forms.CharField(
        widget=forms.Textarea,
        min_length=300,
        error_messages={
            'required': 'Please enter your review',
            'min_length': 'The minimum characters for the review is 300( you have written %(show_value)s)'
        }

    )


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
    
    def clean(self):
        #Super the clean method to obtain main validationand error messages
        super(BookForm, self).clean()

        try:
            title = self.cleaned_data.get('title')
            author = self.cleaned_data.get('author')

            book = Book.objects.get(title = title, author = author)

            raise forms.ValidationError(
                '{} by {} is already exist'.format(title,book.list_authors()),
                code = 'codeexists'
            )

        except Book.DoesNotExist:
            return self.cleaned_data
