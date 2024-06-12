from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Article
import datetime


class ArticleModelTest(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(username="testuser", password="1234")
        self.article = Article.objects.create(
            title="Test Article",
            body="This is body of article",
            slug="test-1",
            author=self.user,
        )

    def test_article_creation(self):
        self.assertEqual(self.article.title, "Test Article")
        self.assertEqual(self.article.body, "This is body of article")
        self.assertEqual(self.article.author.username, "testuser")
        self.assertIsInstance(self.article.date, datetime.datetime)
