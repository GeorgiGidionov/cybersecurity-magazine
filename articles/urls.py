from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('create/', views.ArticleCreateView.as_view(), name='article_create'),

    # Категории – тези трябва да са ПРЕДИ <slug:slug>
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('categories/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/edit/', views.CategoryUpdateView.as_view(), name='category_edit'),
    path('categories/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),

    # Автори
    path('authors/', views.AuthorListView.as_view(), name='author_list'),
    path('authors/create/', views.AuthorCreateView.as_view(), name='author_create'),
    path('authors/<int:pk>/edit/', views.AuthorUpdateView.as_view(), name='author_edit'),
    path('authors/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author_delete'),

    # Детайл на статия (динамичен) – трябва да е СЛЕД статичните
    path('<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('<slug:slug>/edit/', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('<slug:slug>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),
    path('<slug:slug>/comment/', views.add_comment, name='add_comment'),

    # Филтриране по категория
    path('category/<slug:category_slug>/', views.ArticleListView.as_view(), name='article_by_category'),
]