# -*- coding: utf-8 -*-


from django import forms
from django_markdown.widgets import MarkdownWidget


class ArticleForm(forms.Form):
    content = forms.CharField(widget=MarkdownWidget())

