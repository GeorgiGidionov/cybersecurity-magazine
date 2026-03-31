from rest_framework import viewsets, permissions
from articles.models import Article, Comment
from store.models import Product
from .serializers import ArticleSerializer, ProductSerializer, CommentSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.filter(status='published').order_by('-published_at')
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(available=True).order_by('-created_at')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(is_approved=True).order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(is_approved=False)