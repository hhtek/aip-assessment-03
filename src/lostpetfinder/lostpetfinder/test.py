from django.core.urlresolvers import reverse
from django.test import TestCase

class HomeTests(TestCase):
    """
    Test cases to test that the URLs in root urls.py of the project is correct.
    """
    print("------------------------------------------------")
    print("**** Testing project's main URLs of home page ... *****")
    print("------------------------------------------------")

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_lost_pets_view_status_code(self):
        url = reverse('lost-pets')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_reunited_pets_view_status_code(self):
        url = reverse('reunited-pets')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_view_status_code(self):
        url = reverse('about')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_contact_view_status_code(self):
        url = reverse('contact')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_search_pets_view_status_code(self):
        url = reverse('search-pets')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
