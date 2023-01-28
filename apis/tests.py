from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from books.models import Book
from django.urls import reverse



class APITests(APITestCase):
	def setUp(self):
		self.book = Book.objects.create(
			title="Django for APIs",
			author = "William S. Vincent",
			price = "25.00"
		)

	def test_api_list_view(self):
		response = self.client.get(reverse("book_api_list"))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(self.book.title, "Django for APIs")
		self.assertContains(response, self.book)

	def test_api_detail_update_view(self):
		response = self.client.get(
			reverse('book_api_detail_update', kwargs={"pk": self.book.id}),
			format="json"
		)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
