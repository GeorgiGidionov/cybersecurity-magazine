from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.contrib import messages
from .models import Article, Category, Comment
from .forms import ArticleForm, CommentForm
from .tasks import send_comment_notification

class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'articles/article_list.html'
    paginate_by = 9

    def get_queryset(self):
        queryset = Article.objects.filter(status='published').order_by('-published_at')
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(summary__icontains=query) |
                Q(author__name__icontains=query) |
                Q(tags__name__icontains=query)
            ).distinct()
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context

class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'articles/article_detail.html'

    def get_object(self):
        obj = super().get_object()
        obj.views += 1
        obj.save(update_fields=['views'])
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/article_form.html'
    success_url = reverse_lazy('article_list')

class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'articles/article_form.html'
    success_url = reverse_lazy('article_list')

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'articles/article_confirm_delete.html'
    success_url = reverse_lazy('article_list')

def add_comment(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.is_approved = False
            comment.save()
            # Асинхронно изпращане на имейл
            send_comment_notification.delay(comment.id)
            messages.success(request, 'Коментарът е изпратен за одобрение.')
        else:
            messages.error(request, 'Моля, попълнете коректно формата.')
    return redirect('article_detail', slug=slug)

class CommentListView(ListView):
    model = Comment
    template_name = 'articles/comment_list.html'
    context_object_name = 'comments'
    paginate_by = 20

    def get_queryset(self):
        return Comment.objects.all().order_by('-created_at')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'articles/comment_form.html'
    success_url = reverse_lazy('comment_list')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'articles/comment_confirm_delete.html'
    success_url = reverse_lazy('comment_list')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)