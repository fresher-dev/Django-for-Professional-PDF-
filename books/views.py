from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q

class BookListView(LoginRequiredMixin ,ListView):
	model = Book
	context_object_name = "book_list"
	template_name = "books/book_list.html"
	login_url = 'login'


class BookDetailView(
	LoginRequiredMixin,
	DetailView):

	model = Book
	context_object_name = 'book'
	template_name = 'books/book_detail.html'
	login_url = 'login'

class BookUpdateView(UpdateView, PermissionRequiredMixin):
	model = Book
	fields = ["title", "author", "price", "cover"]
	context_object_name = "book"
	template_name = "books/book_update.html"
	permission_required = 'books.special_status'


class SearchResultsListView(ListView):
	model = Book
	context_object_name = "book_list"
	template_name = "books/search_results.html"

	def get_queryset(self):
		query = self.request.GET.get("q")
		return Book.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))
