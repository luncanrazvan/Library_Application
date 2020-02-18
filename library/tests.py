from django.test import TestCase
from selenium import webdriver
from django.test import Client


class FunctionalTestCase(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_there_is_homepage(self):
        self.driver.get('http://127.0.0.1:8000/library/main_page/')
        assert self.driver.page_source.find('borrower')

    def test_borrower_menu(self):
        self.driver.get('http://127.0.0.1:8000/library/borrower_menu')
        assert self.driver.page_source.find('author')

    def tearDown(self):
        self.driver.quit()


class TestRoutes(TestCase):

    def setUp(self):
        self.client = Client()

    def test_borrower_menu_route(self):
        response = self.client.get('/library/borrower_menu/')
        self.assertEqual(response.status_code, 200)

    def test_delete_book_route(self):
        response = self.client.get('/library/librarian_delete/')
        self.assertEqual(response.status_code, 200)


class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_delete_page(self):
        response = self.client.get('/library/librarian_update/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'librarian_update.html')
        self.assertContains(response, 'book_title_old')
