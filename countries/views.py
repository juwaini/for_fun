from django.views.generic import TemplateView
from .models import Country, District, State


class CountryView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['districts'] = District.objects.all().prefetch_related('state', 'state__country')
        return context
