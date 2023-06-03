# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from blog.views import IndexView, BlogDetailView, TagView, ArchiveView, LinkView, SearchView
from blog.views import ArticleAddView
from blog.views import bad_request, page_not_found, permission_denied

# 定义错误跳转页面
handler400 = bad_request
handler403 = permission_denied
handler404 = page_not_found
handler500 = bad_request

app_name = 'blog'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    # 某篇文章的详细信息
    url(r"^post/view/(?P<slug>[\w,-]+)", BlogDetailView.as_view(), name="detail"),
    # 新建文章
    url(r"^post/add/$", ArticleAddView.as_view(), name="add"),
    # 修改文章
    url(r"^post/edit/(?P<pk>\d+)", BlogDetailView.as_view(), name="edit"),
    # 标签信息
    url(r'^tag/$', TagView.as_view(), name="tags"),
    # 某个标签信息
    url(r'^tag/(?P<tag>\w+)', TagView.as_view(), name="tag-detail"),
    # 归档信息
    url(r'^archive/$', ArchiveView.as_view(), name="archive"),
    # 友链信息
    url(r'^link/', LinkView.as_view(), name="link"),
    # 搜索内容
    url(r'^search', SearchView.as_view(), name="search"),
]
