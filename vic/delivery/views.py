from django.views.generic.base import TemplateView


class DeliveryView(TemplateView):
    template_name = 'delivery/delivery.html'


class AirDeliveryView(TemplateView):
    template_name = 'delivery/air.html'


class RoadDeliveryView(TemplateView):
    template_name = 'delivery/road.html'


class TrainDeliveryView(TemplateView):
    template_name = 'delivery/train.html'


class ShipDeliveryView(TemplateView):
    template_name = 'delivery/ship.html'
