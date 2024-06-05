from django.test import SimpleTestCase
from django.urls import resolve, reverse
from ..views import article_create, article_delete, article_detail, article_edit, article_list, article_my_list

class ArticleURLDTest(SimpleTestCase):

    def test_article_list_url(self):
        url = reverse('articles:list')
        self.assertEqual(resolve(url).func, article_list)

    def test_article_mylist_url(self):
        url = reverse('articles:list')
        self.assertEqual(resolve(url).func, article_list)

    def test_article_create_url(self):
        url = reverse('articles:create')
        self.assertEqual(resolve(url).func, article_create)
    
    def test_article_delete_url(self):
        url = reverse('articles:delete', args=[1])
        self.assertEqual(resolve(url).func, article_delete)

    def test_article_detail_url(self):
        url = reverse('articles:detail',  args=['some-slug'])
        self.assertEqual(resolve(url).func, article_detail)

    def test_article_edit_url(self):
        url = reverse('articles:edit', args=[1])
        self.assertEqual(resolve(url).func, article_edit)