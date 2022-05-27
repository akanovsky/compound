from django.urls import path, include
from .views import HomeView,CompoundListView,SetList,CompoundListViewFilter
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = "catalog"

urlpatterns = [
    path("",HomeView.as_view(),name="home"),

    path("filter_compound",CompoundListViewFilter.as_view(), name="filter_compound"),





]
urlpatterns += staticfiles_urlpatterns()