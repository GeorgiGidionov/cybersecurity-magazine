from django import template
from django.utils.html import mark_safe
import markdown
from ..models import Article

register = template.Library()

@register.filter(name='markdown_to_html')
def markdown_to_html(text):
    return mark_safe(markdown.markdown(text))

@register.filter(name='truncate_chars')
def truncate_chars(value, arg):
    try:
        length = int(arg)
    except ValueError:
        return value
    if len(value) > length:
        return value[:length] + '…'
    return value

@register.inclusion_tag('partials/latest_articles.html')
def latest_articles(count=5):
    articles = Article.objects.filter(status='published').order_by('-published_at')[:count]
    return {'latest_articles': articles}