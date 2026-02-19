from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import SubscriptionPlan, Subscription
from .forms import SubscriptionForm

class SubscriptionPlanListView(ListView):
    model = SubscriptionPlan
    context_object_name = 'plans'
    template_name = 'subscriptions/plan_list.html'
    queryset = SubscriptionPlan.objects.filter(is_active=True)

class SubscriptionCreateView(CreateView):
    model = Subscription
    form_class = SubscriptionForm
    template_name = 'subscriptions/subscription_form.html'
    success_url = reverse_lazy('subscription_success')

    def get_initial(self):
        initial = super().get_initial()
        plan_id = self.request.GET.get('plan')
        if plan_id:
            try:
                plan = SubscriptionPlan.objects.get(pk=plan_id)
                initial['plan'] = plan
            except SubscriptionPlan.DoesNotExist:
                pass
        return initial

def subscription_success(request):
    return render(request, 'subscriptions/subscription_success.html')