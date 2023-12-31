from django.test import TestCase
from django.urls import reverse, resolve
from recipes import views


class RecipeViewsTest(TestCase):
    def test_recipe_home_views_functions_is_correct(self):
        view = resolve( reverse('recipes:home'))
        self.assertIs(view.func, views.contato)

    def test_recipe_category_views_functions_is_correct(self):
        view = resolve( reverse('recipes:category', kwargs={'category_id':1}))
        self.assertIs(view.func, views.category)

    def test_recipe_detail_views_functions_is_correct(self):
        view = resolve( reverse('recipes:recipe', kwargs={'id':1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_home_view_returns_status_cod_200_ok(self):
            response = self.client.get(reverse('recipes:home'))
            self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_returns_loads_correct_template(self):
            response = self.client.get(reverse('recipes:home'))
            self.assertTemplateUsed(response, 'home.html')

    def test_recpe_home_no_recipes_found_if_no_template(self):
           response = self.client.get(reverse('recipes:home'))
           self.assertIn('<h1>No recipes found</h1>',response.content.decode('utf-8'))

    def test_recipe_home_view_returns_404_if_not_recipes_found(self):
        response = self.client.get( resolve( reverse('recipes:category', kwargs={'category_id':1})))
        self.assertEqual(response.status_code, 404)
        
    def test_recipe_search_uses_correct_view_function(self):
        url = reverse('recipes:search')
   
        resolved = resolve(url)
        self.assertIs(resolved.func, views.search)
        
    def test_recipe_search_loads_correct_template(self):
        response = self.client.get(reverse('recipes:search'))
        self.assertTemplateUsed(response, 'recipe_category.html')