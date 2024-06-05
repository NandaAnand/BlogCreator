from django.test import TestCase
from ..forms import CreateArticle

class ArticleFormsTest(TestCase):

    def test_article_form_valid(self):
        form = CreateArticle(
            data={
                'title': 'TestTitle',
                'body': 'This is test article body',
                'slug': 'test-article',
                'thumb': ''
            }
        )
        self.assertTrue(form.is_valid())

    def test_article_form_invalid(self):
        form = CreateArticle(
            data={
                'title': '',
                'body': '',
                'slug': '',
                'thumb': ''
            }
        )
        self.assertFalse(form.is_valid())
