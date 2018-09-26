from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


from snippets.views import SnippetViewSet
from rest_framework import renderers

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
snippet_detail = SnippetViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


urlpatterns=[
url(r'^snippets/$',snippet_list,name='Snippet-list'),
url(r'^snippets/(?P<pk>[0-9]+)/$',snippet_detail,name='Snippet-detail'),


]

urlpatterns=format_suffix_patterns(urlpatterns)