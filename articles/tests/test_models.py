from django.test import TestCase
from articles.models import Article, Category, Author, Comment

class ArticleModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Tech')
        self.author = Author.objects.create(name='John')
        self.article = Article.objects.create(
            title='Test Article',
            slug='test-article',
            content='Content',
            category=self.category,
            author=self.author,
            status='published'
        )

    def test_article_str(self):
        self.assertEqual(str(self.article), 'Test Article')