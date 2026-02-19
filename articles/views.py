from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Article, Category
from .forms import ArticleForm
class ArticleDetailView(DetailView):
    model = Article
    context_object_name = 'article'
    template_name = 'articles/article_detail.html'

    def get_object(self):
        obj = super().get_object()
        obj.views += 1
        obj.save(update_fields=['views'])
        return obj

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
        # евентуално филтриране по категория
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context

# Останалите изгледи (DetailView, CreateView, UpdateView, DeleteView) също трябва да са дефинирани,
# за да работят URL адресите. Ако все още не са, добавете ги.