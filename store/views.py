from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Order
from .forms import ProductForm, OrderForm

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'store/product_list.html'
    paginate_by = 12

    def get_queryset(self):
        qs = Product.objects.filter(available=True)

        sort = self.request.GET.get('sort')
        if sort == 'price_asc':
            qs = qs.order_by('price')
        elif sort == 'price_desc':
            qs = qs.order_by('-price')
        else:
            qs = qs.order_by('-created_at')
        return qs

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'store/product_detail.html'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'store/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'store/product_form.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'store/product_confirm_delete.html'
    success_url = reverse_lazy('product_list')

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'store/order_form.html'
    success_url = reverse_lazy('order_success')

def order_success(request):
    return render(request, 'store/order_success.html')