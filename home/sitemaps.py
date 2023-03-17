from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from home.models import Tours


class StaticViewSitemap(Sitemap):
    changefreq = 'hourly'

    def items(self):
        return ['tours', 'contact', 'reservation', 'faq', ]

    def location(self, item):
        return reverse(item)


class ToursSitemap(Sitemap):

    def items(self):
        return Tours.objects.all()
