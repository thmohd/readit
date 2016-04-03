from django.db import models
from django.utils.timezone import now
from django.core.urlresolvers import reverse

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.ManyToManyField('Author', related_name='books')
    review = models.TextField(blank=True, null=True)
    date_review = models.DateTimeField(blank=True, null=True)
    is_favourite = models.BooleanField(default=False, verbose_name="Favourite?")


    def __str__(self):
        return '{} by {}'.format(self.title, self.list_authors())

    def list_authors(self):
        return ', '.join([author.name for author in self.author.all()])


    def save(self, *args, **kwargs):
        if self.review and self.date_review is None:
            self.date_review = now()

        super(Book, self).save(*args, **kwargs)


class Author(models.Model):
    name = models.CharField(max_length=70, help_text="Use pen name rather than real name", unique=True)


    def __str__(self):
        return self.name

    def get_absoulte_url(self):
        return reverse('author-details', kwargs={'pk':self.pk})


