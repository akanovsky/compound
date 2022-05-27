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

class CompoundListViewFilter(LoginRequiredMixin,FilterView):
    model = Compound
    # queryset = Teacher.objects.order_by("first_name")
    template_name = "compound_filter.html"
    filterset_class = SetFilter
    context_object_name = 'compounds'
    paginate_by = 20






class SetList(FilterView):
    model = Compound
    # context_object_name = 'p'
    filterset_class = SetFilter
    paginate_by = 10
    template_name = 'compound_filter.html'
