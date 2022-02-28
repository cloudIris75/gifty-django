from django.views.generic import (
    RedirectView, ListView
)
from menus.models import Brand

class IndexRedirectView(RedirectView):
    pattern_name = 'brand-list'

class BrandListView(ListView):
    model = Brand
    ordering = ['id']
    paginate_by = 6