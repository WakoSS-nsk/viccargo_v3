from django.views.generic.base import TemplateView


class DeliveryView(TemplateView):
    template_name = 'delivery/delivery.html'
