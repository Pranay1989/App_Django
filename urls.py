from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^add/', 'myapp.views.add'),
    url(r'^delete/', 'myapp.views.delete'),
    url(r'^retrieve/', 'myapp.views.retrieve'),  
)
