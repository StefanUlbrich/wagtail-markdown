# vim:sw=4 ts=4 et:
# Copyright (c) 2015 Torchbox Ltd.
# felicity@torchbox.com 2015-09-14
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely. This software is provided 'as-is', without any express or implied
# warranty.
#

from django import template

from ..utils import render_markdown

register = template.Library()


@register.filter(name='markdown')
def markdown(value):
    return render_markdown(value)

# Template tag to load math-related javascript

@register.inclusion_tag('wagtailmarkdown/load_markdown_math.html')
def load_markdown_math():
    return {}
