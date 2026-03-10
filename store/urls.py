from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('create/', views.ProductCreateView.as_view(), name='product_create'),          # ← първо
    path('<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),    # ← после
    path('<slug:slug>/edit/', views.ProductUpdateView.as_view(), name='product_edit'),
    path('<slug:slug>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
]