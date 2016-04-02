from django import forms

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
