from django.urls import path
from . import views

urlpatterns = [
    path('', views.SubscriptionPlanListView.as_view(), name='plan_list'),
    path('subscribe/', views.SubscriptionCreateView.as_view(), name='subscription_create'),
    path('success/', views.subscription_success, name='subscription_success'),
]