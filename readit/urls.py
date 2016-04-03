"""readit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from books.views import (BookDetails, AuthorDetails, CreateAuthor, list_books, AuthorsList,
                         ReviewList, review_book)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', list_books, name="books"),
    url(r'^authors/add/$', CreateAuthor.as_view(), name="add-author"),
    url(r'^authors/$', AuthorsList.as_view(), name='authors'),
    url(r'^books/(?P<pk>[-\w])/$', BookDetails.as_view(), name="book_details"),
    url(r'^author/(?P<pk>[-\w])/$', AuthorDetails.as_view(), name="author_details"),
    url(r'^review/$', ReviewList.as_view(), name='review-books'),
    url(r'^review/(?P<pk>[-\w]+)/$', review_book, name='review-book'),
]
