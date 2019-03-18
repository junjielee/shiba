# -*- coding: utf-8 -*-

from django.template import Library
from django.template.defaultfilters import stringfilter
# from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

# from markdown import markdown
# from mistune import Markdown
import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import html


register = Library()


class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code>code></pre>pre>\n' % \
                mistune.escape(code)
        lexer = get_lexer_by_name(lang, stripall=True)
        formatter = html.HtmlFormatter(style='monokai')
        return highlight(code, lexer, formatter)


renderer = HighlightRenderer()
markdown = mistune.Markdown(renderer=renderer)


@register.filter(is_safe=True)
@stringfilter
def markdown_change(md):
    # return mark_safe(markdown(force_unicode(md)))
    return mark_safe(markdown(md))
