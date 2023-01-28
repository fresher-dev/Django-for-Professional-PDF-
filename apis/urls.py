from django.urls import path
from .views import BookAPIView, BookDetailUpdateAPIView


urlpatterns = [
	path("", BookAPIView.as_view(), name="book_api_list"),
	path("<uuid:pk>/", BookDetailUpdateAPIView.as_view(), name="book_api_detail_update"),
]