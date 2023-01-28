from django.shortcuts import render
from rest_framework import generics, permissions
from books.models import Book
from .serializers import BookSerializer


class BookAPIView(generics.ListAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer


class BookDetailUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
	permission_class = (permissions.IsAdminUser,)
	queryset = Book.objects.all()
	serializer_class = BookSerializer
