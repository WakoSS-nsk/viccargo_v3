from django.views.generic.base import TemplateView


class ReviewsView(TemplateView):
    template_name = 'reviews/reviews.html'
