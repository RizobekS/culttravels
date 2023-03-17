from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from home.sitemaps import StaticViewSitemap, ToursSitemap

from home.models import FAQ, Tours, Contact, Reservation, MyTours

sitemaps = {
    'static': StaticViewSitemap,
    'tours': ToursSitemap
}

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('api/transaction/', include("transaction.urls")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    prefix_default_language=True,
)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
