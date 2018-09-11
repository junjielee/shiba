# -*- coding: utf-8 -*-

from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class TimeBaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True, blank=True)
    slug = models.CharField(_('Slug'), max_length=100, unique=True)

    class Meta:
        abstract = True


class Category(TimeBaseModel):
    name = models.CharField(_('Category Name'), max_length=100, unique=True)
    description = models.TextField(_('Category Description'), max_length=1024)

    def __str__(self):
        return self.name

    class Meta(TimeBaseModel.Meta):
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Tag(TimeBaseModel):
    name = models.CharField(_('Tag Name'), max_length=100, unique=True)
    bg_color = models.CharField(_("Bg color name"), max_length=50, default="blue-grey")
    text_color = models.CharField(_("text color name"), max_length=50, default="white-text")

    def __str__(self):
        return self.name

    class Meta(TimeBaseModel.Meta):
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class Article(TimeBaseModel):
    title = models.CharField(_('Article Title'), max_length=100, unique=True)
    category = models.ForeignKey(Category, verbose_name=_('Article Category'), null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, verbose_name=_('Article Tags'),
                                  blank=True)
    enable_comment = models.BooleanField(_('Enable Comment'), default=True)
    pubished = models.BooleanField(_('Is Publish'), default=True)
    file_used = models.BooleanField(_('Is file used'), default=True)
    content = models.TextField(blank=True)
    content_file = models.FileField(upload_to='articles/',
                                    verbose_name=_('Content File'),
                                    blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.file_used:
            content = self.content_file.read()
            if isinstance(content, bytes):
                content = content.decode('utf8')
            self.content = content
        super(Article, self).save(*args, **kwargs)

    def get_tags(self):
        tags = self.tags.all()
        counts = len(tags)
        tags_text = ''
        for i in range(counts):
            tags_text += tags[i].name
            if i != (counts - 1):
                tags_text += ','
        return tags_text

    def get_absolute_url(self):
        return reverse('blog.article', args=(self.slug, ))

    class Meta(TimeBaseModel.Meta):
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        ordering = ['-create_time', ]
