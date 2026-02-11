from django.shortcuts import render
from articles.models import Article
from store.models import Product

def home(request):
    featured_articles = Article.objects.filter(featured=True, status='published')[:3]
    latest_products = Product.objects.filter(available=True).order_by('-created_at')[:4]
    return render(request, 'index.html', {
        'featured_articles': featured_articles,
        'latest_products': latest_products,
    })

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')