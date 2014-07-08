from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

from AssetManager.core.accounts.urls import router as accounts_router
from AssetManager.apps.assets.urls import router as assets_router


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'AssetManager.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Django Core
    url(r'^admin/', include(admin.site.urls)),

    # 3rd-Party Extensions
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Project apps
    url(r'^', include(accounts_router.urls)),
    url(r'^', include(assets_router.urls)),
)


# 3rd party extensions
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
