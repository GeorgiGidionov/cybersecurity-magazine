from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from articles.models import Article, Category, Author
from django.contrib.auth.models import User

class ArticleAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()  # ← създаваме APIClient за всеки тест
        self.username = 'apiuser'
        self.user = User.objects.create_user(username=self.username, password='pass')
        self.category = Category.objects.create(name='Tech')
        self.author = Author.objects.create(name='John')
        self.article = Article.objects.create(
            title='API Test',
            slug='api-test',
            content='Content',
            category=self.category,
            author=self.author,
            status='published'
        )

    def test_get_articles_list(self):
        url = reverse('article-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data['results']), 1)

    def test_create_article_requires_auth(self):
        url = reverse('article-list')
        data = {
            'title': 'New',
            'slug': 'new',
            'content': 'New content',
            'category': self.category.id,
            'author': self.author.id,
            'status': 'draft'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_article_authenticated(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('article-list')
        data = {
            'title': 'Auth Article',
            'slug': 'auth-article',
            'content': 'Auth content',
            'category': self.category.id,
            'author': self.author.id,
            'status': 'draft'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)