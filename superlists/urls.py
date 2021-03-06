from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    # Examples:
    # url(r'^$', 'superlists.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'lists.views.home_page', name='home'),
    url(r'^lists/(.+)/$', 'lists.views.view_list',
        name='view_list'),
    url(r'^lists/new$', 'lists.views.new_list', name='new_list'),

]
