from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail')
]