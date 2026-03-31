from django.test import TestCase, override_settings
from django.contrib.auth.models import User
from articles.models import Article, Comment
from articles.tasks import send_comment_notification

@override_settings(CELERY_TASK_ALWAYS_EAGER=True)
class AsyncTaskTest(TestCase):
    def setUp(self):
        self.article = Article.objects.create(
            title='Task Test',
            slug='task-test',
            content='Content',
            status='published'
        )
        self.comment = Comment.objects.create(
            article=self.article,
            author_name='Tester',
            content='Hello'
        )

    def test_send_notification_called(self):
        # Задачата ще се изпълни синхронно
        result = send_comment_notification.delay(self.comment.id)
        self.assertIsNone(result.result)  # или проверете, че задачата е изпълнена успешно