from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('create/', views.ProductCreateView.as_view(), name='product_create'),
    path('order/success/', views.order_success, name='order_success'),

    # Категории продукти – статични маршрути, които трябва да са ПРЕДИ <slug:slug>
    path('product-categories/', views.ProductCategoryListView.as_view(), name='productcategory_list'),
    path('product-categories/create/', views.ProductCategoryCreateView.as_view(), name='productcategory_create'),
    path('product-categories/<int:pk>/edit/', views.ProductCategoryUpdateView.as_view(), name='productcategory_edit'),
    path('product-categories/<int:pk>/delete/', views.ProductCategoryDeleteView.as_view(), name='productcategory_delete'),

    # Динамични маршрути за продукти (трябва да са СЛЕД статичните)
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('<slug:slug>/edit/', views.ProductUpdateView.as_view(), name='product_edit'),
    path('<slug:slug>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('<slug:slug>/order/', views.OrderCreateView.as_view(), name='order_create'),
]