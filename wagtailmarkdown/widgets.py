# vim:sw=4 ts=4 et:
# Copyright (c) 2015 Torchbox Ltd.
# tomasz.knapik@torchbox.com 2017-12-07
#
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely. This software is provided 'as-is', without any express or implied
# warranty.
#
from django import forms
from django.conf import settings

from wagtail.utils.widgets import WidgetWithScript


class MarkdownTextarea(WidgetWithScript, forms.widgets.Textarea):
    def __init__(self, **kwargs):
        super(MarkdownTextarea, self).__init__(**kwargs)

    def render_js_init(self, id_, name, value):
        return 'easymdeAttach("{0}");'.format(id_)

    @property
    def media(self):
        js = [
            'wagtailmarkdown/js/easymde.attach.js',
            'wagtailmarkdown/js/easymde.min.js',
        ]

        if getattr(settings, 'WAGTAILMARKDOWN_USE_MATH', False):
            js += [
                'wagtailmarkdown/js/MathJax.js'
                'wagtailmarkdown/js/arithmatex.js'
            ]

        return forms.Media(
            css = {
                'all': (
                    'wagtailmarkdown/css/easymde.min.css',
                )
            },
            js = js
        )
