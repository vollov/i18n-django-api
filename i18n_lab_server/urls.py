# from django.conf.urls import patterns, include, url
# from django.contrib import admin
# 
# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'i18n_lab_server.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
# 
#     url(r'^admin/', include(admin.site.urls)),
# )

from django.conf.urls import url, include
from rest_framework import routers
from django.contrib import admin
from quickstart import views as quickstart_views
from page import views as page_views

router = routers.DefaultRouter()
router.register(r'users', quickstart_views.UserViewSet)
router.register(r'groups', quickstart_views.GroupViewSet)
router.register(r'pages', page_views.PageViewSet)
router.register(r'paget', page_views.PageTranslationViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/pages/(?P<lang>[a-z][a-z])/$', page_views.PageView.as_view()),
]