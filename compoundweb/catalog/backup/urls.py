from django.urls import path, include
from .views import HomeView,CompoundListView,SetList,FilteredListView,CompoundListViewFilter
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "catalog"

urlpatterns = [
    path("",HomeView.as_view(),name="home"),
    path("list_compound", FilteredListView.as_view(), name="list_compound"),
    path("filter_compound",CompoundListViewFilter.as_view(), name="filter_compound"),





]
urlpatterns += staticfiles_urlpatterns()