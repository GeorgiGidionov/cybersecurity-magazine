from rest_framework import serializers
from articles.models import Article, Category, Author, Tag, Comment
from store.models import Product, ProductCategory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'bio', 'email', 'website']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author_name', 'author_email', 'content', 'created_at', 'is_approved']
        read_only_fields = ['created_at', 'is_approved']

class ArticleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    author = AuthorSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'content', 'summary', 'category', 'author', 'tags',
                  'created_at', 'updated_at', 'published_at', 'status', 'views', 'featured',
                  'comments']
        read_only_fields = ['slug', 'views', 'comments']

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name', 'description']

class ProductSerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'description', 'price', 'category', 'stock', 'available',
                  'created_at', 'updated_at', 'image']