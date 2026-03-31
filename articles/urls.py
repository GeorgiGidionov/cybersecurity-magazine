from django.urls import path
from . import views

urlpatterns = [
    # Списък със статии
    path('', views.ArticleListView.as_view(), name='article_list'),
    # Създаване на нова статия
    path('create/', views.ArticleCreateView.as_view(), name='article_create'),
    # Детайли на статия (трябва да е след create, за да не се обърка)
    path('<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
    # Добавяне на коментар към статия
    path('<slug:slug>/comment/', views.add_comment, name='add_comment'),
    # Редакция на статия
    path('<slug:slug>/edit/', views.ArticleUpdateView.as_view(), name='article_edit'),
    # Изтриване на статия
    path('<slug:slug>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),
    # Филтриране по категория
    path('category/<slug:category_slug>/', views.ArticleListView.as_view(), name='article_by_category'),
    # Управление на коментари (само за суперпотребители)
    path('comments/', views.CommentListView.as_view(), name='comment_list'),
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_edit'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
]