from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from model_report import report
report.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'moneySaver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^reports', include('model_report.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('ticket.urls')),
]
