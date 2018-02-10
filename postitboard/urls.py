from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework.routers import DefaultRouter

from .api import GroupViewSet, DetailsView

urlpatterns = {
  url(r'^groups/$', GroupViewSet.as_view(), name="group"),
  url(r'^groups/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details")
}

""" The format_suffix_pattern allows us to specify the data format (raw json or even html) when we use the URLs. It appends the format to be used to every URL in the pattern."""
urlpatterns = format_suffix_patterns(urlpatterns)

# router = DefaultRouter()

# router.register(r'groups', GroupViewSet)
# router.register(r'messages', MessageViewSet)

# urlpatterns = router.urls
