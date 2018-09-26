from django.conf.urls import url,include
from django.contrib.auth  import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(),name="index"),
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name="details"),
    url(r'^album/add/$',views.AlbumCreate.as_view(),name='album-add'),
    url(r'^login/$',auth_views.login,{'template_name':'music/login_user.html'}),
    url(r'^logout/$',auth_views.logout,{'next_page':'/'}),
    url(r'^register/$',views.register,name='register'),


]