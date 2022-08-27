from django.views.generic.base import TemplateView


class PackingView(TemplateView):
    template_name = 'packing/packing.html'
