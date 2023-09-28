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
        
    def test_recipe_search_is_correct(self):
         url = reverse('recipes:search')
         self.assertEqual(url, '/recipes/search/')

    def test_recipe_search_raises_404_if_no_search_term(self):
        url = reverse('recipes:search')
        response= self.client.get(url)
        self.assertEqual(response.status_code, 404)