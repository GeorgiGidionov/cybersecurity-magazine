from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('create/', views.ProductCreateView.as_view(), name='product_create'),
    path('<slug:slug>/edit/', views.ProductUpdateView.as_view(), name='product_edit'),
    path('<slug:slug>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('order/<slug:slug>/', views.OrderCreateView.as_view(), name='order_create'),
    path('order/success/', views.order_success, name='order_success'),
]