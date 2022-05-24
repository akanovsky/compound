import django_filters
from .models import Compound




class SetFilter(django_filters.FilterSet):
    c_set = django_filters.AllValuesFilter()
    class Meta:
        model = Compound
        fields = ['c_set']

