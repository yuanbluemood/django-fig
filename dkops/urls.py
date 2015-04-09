from django.conf.urls import patterns, include, url
from django.contrib import admin
from dkops import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dkops.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home,name='home'),
    url(r'^overview/', views.overview,name='overview'),
    url(r'^myapp/', views.myapp,name='myapp'),
    url(r'^myservice/', views.myservice,name='myservice'),
)
