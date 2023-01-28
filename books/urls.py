from django.urls import path
from .views import BookListView, BookDetailView, SearchResultsListView, BookUpdateView


urlpatterns = [
	path("", BookListView.as_view(), name="book_list"),
	path("<uuid:pk>/", BookDetailView.as_view(), name="book_detail"),
	path("search/", SearchResultsListView.as_view(), name="search"),
	path("update/<uuid:pk>/", BookUpdateView.as_view(), name="book_update"),
]