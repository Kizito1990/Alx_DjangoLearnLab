from rest_framework import status



class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")
        
        # Create sample books
        self.book1 = Book.objects.create(title="Book One", author="Author A", publication_year=2020)
        self.book2 = Book.objects.create(title="Book Two", author="Author B", publication_year=2021)

        # Endpoints
        self.list_url = reverse('book-list')  # Adjust name based on urlpatterns
        self.detail_url = lambda pk: reverse('book-detail', kwargs={'pk': pk})

    def tearDown(self):
        self.user.delete()
        Book.objects.all().delete()


   def test_create_book(self):
       data = {
           "title": "New Book",
           "author": "Author C",
           "publication_year": 2022
       }
       response = self.client.post(self.list_url, data)
       self.assertEqual(response.status_code, status.HTTP_201_CREATED)
       self.assertEqual(Book.objects.count(), 3)
       self.assertEqual(Book.objects.last().title, "New Book")


   def test_retrieve_book(self):
       response = self.client.get(self.detail_url(self.book1.id))
       self.assertEqual(response.status_code, status.HTTP_200_OK)
       self.assertEqual(response.data['title'], self.book1.title)



   def test_update_book(self):
       data = {"title": "Updated Title"}
       response = self.client.patch(self.detail_url(self.book1.id), data)
       self.assertEqual(response.status_code, status.HTTP_200_OK)
       self.book1.refresh_from_db()
       self.assertEqual(self.book1.title, "Updated Title")


   def test_delete_book(self):
       response = self.client.delete(self.detail_url(self.book1.id))
       self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
       self.assertEqual(Book.objects.count(), 1)


   def test_filter_books_by_author(self):
       response = self.client.get(f"{self.list_url}?author=Author A")
       self.assertEqual(response.status_code, status.HTTP_200_OK)
       self.assertEqual(len(response.data), 1)
       self.assertEqual(response.data[0]['author'], "Author A")



   def test_search_books(self):
       response = self.client.get(f"{self.list_url}?search=Book One")
       self.assertEqual(response.status_code, status.HTTP_200_OK)
       self.assertEqual(len(response.data), 1)
       self.assertEqual(response.data[0]['title'], "Book One")


   def test_order_books_by_publication_year(self):
       response = self.client.get(f"{self.list_url}?ordering=-publication_year")
       self.assertEqual(response.status_code, status.HTTP_200_OK)
       self.assertEqual(response.data[0]['publication_year'], 2021)


   def test_unauthenticated_access(self):
       self.client.logout()
       response = self.client.get(self.list_url)
       self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

