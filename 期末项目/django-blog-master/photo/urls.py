# -*- coding: utf-8 -*-

from django.conf.urls import url
from photo.views import PhotoGroupView, PhotoView, UploadView

app_name = 'photo'
urlpatterns = [
    url(r'^$', PhotoGroupView.as_view(), name="photogroup"),
    # 显示图片列表0
    url(r'^photo/(?P<group>\w+)/$', PhotoView.as_view(), name="photo"),
    # 上传图片
    url(r'^upload/$', UploadView.as_view(), name="upload"),
]
