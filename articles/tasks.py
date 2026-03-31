from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_comment_notification(comment_id):
    from .models import Comment
    comment = Comment.objects.get(id=comment_id)
    subject = f'New comment on "{comment.article.title}"'
    message = f'A new comment by {comment.author_name}:\n\n{comment.content}'
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [settings.ADMIN_EMAIL],  # или някакъв списък с имейли
        fail_silently=False,
    )