from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Article
from ..forms import CreateArticle


class ArticleViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='1234')
        self.client.login(username='testuser', password='1234')
        self.article = Article.objects.create(
             title = 'Test Article',
            body = 'This is body of article',
            slug = 'test-1',
            author = self.user
        )
        self.valid_data = {
            'title': 'Updated Title',
            'body': 'Updated body.',
            'slug': 'updated-title',
        }
    
    def test_article_list_view(self):
        response = self.client.get(reverse('articles:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/article_list.html')
    
    def test_article_mylist_view(self):
        response = self.client.get(reverse('articles:list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/article_list.html')

    def test_article_detail_view(self):
        
        response = self.client.get(reverse('articles:detail', kwargs={'slug': self.article.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/article_detail.html')
        self.assertContains(response, self.article.title)
        self.assertContains(response, self.article.body)
        self.assertContains(response, self.article.author.username)

    def test_article_create_view(self):
        
        response = self.client.get(reverse('articles:create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/article_create.html')
        self.assertIsInstance(response.context['form'], CreateArticle)

    def test_create_article_view_post_valid_data(self):
        response = self.client.post(reverse('articles:create'), data=self.valid_data)
        self.assertEqual(response.status_code, 302)  # Should redirect after successful creation
        self.assertTrue(Article.objects.filter(title='Test Article').exists())

    def test_create_article_view_no_login(self):
        self.client.logout()
        response = self.client.get(reverse('articles:create'))
        self.assertRedirects(response, f'/accounts/login/?next=/articles/create/')

    def test_article_edit_view(self):
    
        response = self.client.get(reverse('articles:edit', args=[self.article.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'articles/article_edit.html')
        self.assertIsInstance(response.context['form'], CreateArticle)

    def test_edit_article_view_post_valid_data(self):
        response = self.client.post(reverse('articles:edit', args=[self.article.id]), data=self.valid_data)
        self.assertEqual(response.status_code, 302)  # Should redirect after successful edit
        self.article.refresh_from_db()
        self.assertEqual(self.article.title, 'Updated Title')
        self.assertEqual(self.article.body, 'Updated body.')
    
    def test_edit_article_view_no_login(self):
        self.client.logout()
        response = self.client.get(reverse('articles:edit', args=[self.article.id]))
        self.assertRedirects(response, f'/accounts/login/?next=/articles/{self.article.id}/edit/')

    def test_article_delete_view(self):
    
        response = self.client.post(reverse('articles:delete', args=[self.article.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Article.objects.filter(id=self.article.id).exists())
        
    def test_delete_article_view_no_login(self):
        self.client.logout()
        response = self.client.get(reverse('articles:delete', args=[self.article.id]))
        self.assertRedirects(response, f'/accounts/login/?next=/articles/{self.article.id}/delete/')

