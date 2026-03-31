from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from articles.models import Category, Author, Article, Comment

class ArticleListViewTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Tech')
        self.author = Author.objects.create(name='John')
        self.article = Article.objects.create(
            title='Published',
            slug='published',
            content='Content',
            category=self.category,
            author=self.author,
            status='published'
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/articles/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('article_list'))
        self.assertTemplateUsed(response, 'articles/article_list.html')

    def test_article_list_contains_published_articles(self):
        response = self.client.get(reverse('article_list'))
        self.assertContains(response, 'Published')

    def test_search_functionality(self):
        response = self.client.get(reverse('article_list'), {'q': 'Published'})
        self.assertContains(response, 'Published')
        response = self.client.get(reverse('article_list'), {'q': 'nonexistent'})
        self.assertNotContains(response, 'Published')

class ArticleDetailViewTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='John')
        self.article = Article.objects.create(
            title='Detail',
            slug='detail',
            content='Detail content',
            author=self.author,
            status='published'
        )

    def test_view_returns_correct_article(self):
        response = self.client.get(reverse('article_detail', args=['detail']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Detail content')

    def test_view_increments_views(self):
        initial = self.article.views
        self.client.get(reverse('article_detail', args=['detail']))
        self.article.refresh_from_db()
        self.assertEqual(self.article.views, initial + 1)

class AddCommentTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='John')
        self.article = Article.objects.create(
            title='Commentable',
            slug='commentable',
            content='Text',
            author=self.author,
            status='published'
        )
        self.url = reverse('add_comment', args=['commentable'])

    def test_comment_addition(self):
        response = self.client.post(self.url, {
            'author_name': 'Tester',
            'content': 'Great article!'
        })
        self.assertEqual(response.status_code, 302)  # redirect
        self.assertTrue(Comment.objects.filter(content='Great article!').exists())

    def test_comment_without_name_fails(self):
        response = self.client.post(self.url, {
            'content': 'No name'
        })
        self.assertEqual(Comment.objects.count(), 0)