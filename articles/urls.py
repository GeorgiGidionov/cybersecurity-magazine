from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('create/', views.ArticleCreateView.as_view(), name='article_create'),

    # Детайли, редакция, изтриване на статия
    path('<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('<slug:slug>/edit/', views.ArticleUpdateView.as_view(), name='article_edit'),
    path('<slug:slug>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),
    path('<slug:slug>/comment/', views.add_comment, name='add_comment'),

    # Коментари (само за суперпотребител)
    path('comments/', views.CommentListView.as_view(), name='comment_list'),
    path('comments/<int:pk>/edit/', views.CommentUpdateView.as_view(), name='comment_edit'),
    path('comments/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),

    # Филтър по категория (ако искате да запазите – но категориите може да са празни)
    path('category/<slug:category_slug>/', views.ArticleListView.as_view(), name='article_by_category'),
]