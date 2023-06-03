# -*- coding: utf-8 -*-

import datetime
import markdown
from django.db import models
from uuslug import slugify
from blog.storage import PathAndRename
from django.urls import reverse
from mdeditor.fields import MDTextField
from taggit.managers import TaggableManager

BlogTypes = (
    ('d', 'Django学习'),
    ('j', 'Java学习'),
    ('f', '前端学习'),
    ('l', 'Linux学习'),
    ('r', 'Redis学习')
)


class Article(models.Model):
    name = models.CharField(u'标题', max_length=150, unique=True)
    # 访问文章的短链接 http://127.0.0.1:8000/post/view/django-study-01
    slug = models.SlugField(u'链接', default='#', null=True, blank=True)
    # 上传到/upload/cover
    cover = models.ImageField(upload_to=PathAndRename("cover"), verbose_name=u'封面')
    # 文章类型
    type = models.CharField(max_length=1, choices=BlogTypes, default='d', verbose_name=u'类型')
    # 文章内容
    content = MDTextField(u'内容', )
    # 文章摘要
    excerpt = models.TextField(u'摘要', )
    create_time = models.DateTimeField(u'创建时间', auto_now_add=True)
    update_time = models.DateTimeField(u'修改时间')
    # 是否发布
    published = models.BooleanField(u'发布', default=True)
    # 是否置顶
    is_top = models.BooleanField(u'置顶', default=False)
    # 是否开启评论
    allow_comments = models.BooleanField('开启评论', default=True)
    # 发布时间
    publish_time = models.DateTimeField(u'发布时间', null=True)
    # 浏览量
    views = models.PositiveIntegerField(u'浏览量', default=0)
    tags = TaggableManager(blank=True, help_text='标签用英文逗号隔开')

    class Meta:
        # 降序
        ordering = ['-is_top', '-update_time']
        # verbose_name指定在admin管理界面中显示中文
        verbose_name = u'文章'
        verbose_name_plural = u'文章'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        modified = kwargs.pop("modified", True)
        # 是否修改
        if modified:
            self.update_time = datetime.datetime.utcnow()
        # 是否发布
        if self.published and not self.publish_time:
            self.publish_time = datetime.datetime.utcnow()

        # 生成摘要
        # 获取readmore位置 ‘阅读更多’
        readmore_index = self.content.find('<!--more-->')

        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.toc',
            'markdown.extensions.headerid',
        ])
        # 截取readmore前的字符串作为摘要并用markdown渲染
        self.excerpt = md.convert(self.content[:readmore_index])
        # 保存数据库
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'slug': self.slug})


class Friend(models.Model):
    """
    友情链接
    """
    name = models.CharField(u'名称', max_length=100, default='')
    link = models.URLField(u'链接', default='')
    cover = models.ImageField(upload_to=PathAndRename("link"), blank=True, verbose_name=u'头像')
    desc = models.TextField(u'描述', default='未添加描述')
    # 从左向右123开始...
    position = models.SmallIntegerField(u'位置', default=1)
    active = models.BooleanField(u'激活', default=True)

    class Meta:
        ordering = ['position']
        verbose_name = u'友情链接'
        verbose_name_plural = u'友情链接'

    def __str__(self):
        return self.name


class Social(models.Model):
    """
    社交网站
    """
    name = models.CharField(u'名称', max_length=10, unique=True)
    url = models.CharField(u'地址', max_length=50, unique=True)
    cover = models.ImageField(upload_to=PathAndRename("social"), blank=True, verbose_name=u'图标')
    # 从左向右123...
    position = models.SmallIntegerField(u'位置', default=1)

    class Meta:
        ordering = ['-position']
        verbose_name = u'社交网站'
        verbose_name_plural = u'社交网站'

    def __str__(self):
        return self.name
