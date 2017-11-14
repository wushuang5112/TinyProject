from django.conf.urls import include, url, handler404, handler500  # noqa
from demoapp import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = (
    # Examples:
    # url(r'^$', 'proj.views.home', name='home'),
    # url(r'^proj/', include('proj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^task/', include('demotask.urls')),
)
