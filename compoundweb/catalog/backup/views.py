from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from catalog.models import Compound
from django_filters.views import FilterView
from .filters import SetFilter
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class HomeView(TemplateView):
    template_name = "catalog/home.html"

class CompoundListView(LoginRequiredMixin,ListView):
    model = Compound
    # queryset = Teacher.objects.order_by("first_name")
    myFilter = SetFilter
    paginate_by = 20

    # context_object_name = "list_compound"

class FilteredListView(LoginRequiredMixin,ListView):
    filterset_class = None

    def get_queryset(self):
        # Get the queryset however you usually would.  For example:
        queryset = super().get_queryset()
        # Then use the query parameters and the queryset to
        # instantiate a filterset and save it as an attribute
        # on the view instance for later.
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        # Return the filtered queryset
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Pass the filterset to the template - it provides the form.
        context['filterset'] = self.filterset
        return context





# class SetList(FilterView):
class SetList(FilterView):
    model = Compound
    # context_object_name = 'p'
    filterset_class = SetFilter
    paginate_by = 20
    template_name = 'compound_filter.html'
