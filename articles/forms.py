from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'slug', 'content', 'summary', 'category', 'author', 'status', 'featured']
        exclude = ['created_at', 'updated_at', 'views', 'published_at']  # изключени полета
        widgets = {
            'content': forms.Textarea(attrs={'rows': 10, 'placeholder': 'Write your article content here...'}),
            'summary': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Brief summary (max 500 chars)'}),
        }
        labels = {
            'title': 'Article Title',
            'slug': 'URL Slug',
            'content': 'Full Article',
            'summary': 'Short Summary',
            'category': 'Select Category',
            'author': 'Author',
            'status': 'Publication Status',
            'featured': 'Feature on Homepage?',
        }
        help_texts = {
            'slug': 'Unique identifier for the URL. Use lowercase letters, numbers and hyphens.',
            'status': 'Draft – only you can see; Published – visible to everyone.',
        }
        error_messages = {
            'title': {
                'required': 'Please give your article a title.',
                'max_length': 'Title is too long (max 200 characters).',
            },
            'slug': {
                'unique': 'This slug is already used. Please choose another one.',
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk and self.instance.status == 'published':
            self.fields['status'].disabled = True
            self.fields['status'].help_text = 'Cannot change status of a published article.'