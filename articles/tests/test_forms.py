from django.test import TestCase
from articles.forms import ArticleForm, CommentForm
from articles.models import Category, Author

class ArticleFormTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Tech')
        self.author = Author.objects.create(name='Writer')

    def test_valid_article_form(self):
        data = {
            'title': 'New Article',
            'slug': 'new-article',
            'content': 'Some content',
            'summary': 'Short',
            'category': self.category.id,
            'author': self.author.id,
            'status': 'draft',
            'featured': False,
        }
        form = ArticleForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_article_form_missing_title(self):
        data = {
            'slug': 'new-article',
            'content': 'Some content',
            'category': self.category.id,
            'author': self.author.id,
        }
        form = ArticleForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

class CommentFormTest(TestCase):
    def test_valid_comment_form(self):
        data = {'author_name': 'Ivan', 'content': 'Nice!'}
        form = CommentForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_comment_form_missing_name(self):
        data = {'content': 'Nice!'}
        form = CommentForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('author_name', form.errors)