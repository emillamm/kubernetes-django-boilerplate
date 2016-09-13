from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()
from django.views.static import serve
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from my_backend.apps.blog.views import BlogPostViewSet

router = routers.SimpleRouter()

router.register(r'^blogposts', BlogPostViewSet)

api_urlpatterns = router.urls
api_urlpatterns = format_suffix_patterns(api_urlpatterns)



urlpatterns = [
    # General
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(api_urlpatterns)),

    # Apps
    url(r'^markdownx/', include('markdownx.urls')),
]

# support media files in DEBUG mode
from django.conf import settings
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$',
            serve, {'document_root': settings.MEDIA_ROOT})]