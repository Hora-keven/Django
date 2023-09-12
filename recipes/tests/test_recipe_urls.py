from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class RecipeURLstest(TestCase):

    def test_recip_home_url_is_correct(self):
        home_url = reverse('recipes:home')
        self.assertEqual(home_url, '/')

    def test_recip_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id':1})
        self.assertEqual(url, '/recipe/category/1/')

    def test_recip_detail_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id':1})
        self.assertEqual(url, '/recipe/1/')