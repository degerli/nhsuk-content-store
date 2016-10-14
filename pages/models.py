import re

from django.db import models
from django.utils.translation import ugettext_lazy
from wagtail.wagtailadmin.edit_handlers import (
    FieldPanel, MultiFieldPanel, StreamFieldPanel
)
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page

from images.blocks import ImageChooserBlock
from wagtailmarkdown.fields import MarkdownBlock

from .blocks import ListBlock, StreamBlock

LABEL_RE = re.compile("([a-z])([A-Z])")


class Components(object):
    TYPES = {
        'markdown': MarkdownBlock,
        'calloutInfo': MarkdownBlock,
        'calloutWarning': MarkdownBlock,
        'calloutAlert': MarkdownBlock,
        'figureList': lambda **kwargs: ListBlock(ImageChooserBlock(), **kwargs)
    }

    @classmethod
    def get(cls, _type):
        label = LABEL_RE.sub("\g<1> \g<2>", _type).lower()
        return (_type, cls.TYPES[_type](label=label))


class SimplePage(Page):
    SIDEBAR_ORDER_LAST = 'last'
    SIDEBAR_ORDER_FIRST = 'first'
    SIDEBAR_ORDER_CHOICES = (
        (SIDEBAR_ORDER_LAST, 'Last'),
        (SIDEBAR_ORDER_FIRST, 'First'),
    )

    # META
    sidebar_order = models.CharField(
        max_length=50,
        choices=SIDEBAR_ORDER_CHOICES,
        default=SIDEBAR_ORDER_LAST
    )
    non_emergency_callout = models.BooleanField(
        default=True,
        verbose_name='Non-emergency callout',
        help_text='Shows/hides the call 111 section'
    )
    choices_origin = models.CharField(
        max_length=255, blank=True,
        help_text=(
            'Optional. Related Choices page '
            '(e.g. conditions/stomach-ache-abdominal-pain/Pages/Introduction.aspx)'
        )
    )

    # CONTENT BLOCKS
    before = StreamField(
        StreamBlock([
            Components.get('markdown'),
            Components.get('figureList'),
        ]), null=True, blank=True
    )

    local_header = StreamField(
        StreamBlock([
            Components.get('markdown')
        ]), null=True, blank=True
    )

    main = StreamField(
        StreamBlock([
            Components.get('markdown'),
            Components.get('calloutInfo'),
            Components.get('calloutWarning'),
        ]), null=True, blank=True
    )

    sidebar = StreamField(
        StreamBlock([
            Components.get('markdown'),
            Components.get('calloutAlert'),
        ]), null=True, blank=True
    )

    # PANELS
    content_panels = [
        MultiFieldPanel([
            FieldPanel('title'),
            FieldPanel('sidebar_order'),
        ]),
        StreamFieldPanel('local_header'),
        StreamFieldPanel('before'),
        StreamFieldPanel('main'),
        StreamFieldPanel('sidebar')
    ]

    promote_panels = [
        MultiFieldPanel([
            FieldPanel('non_emergency_callout'),
            FieldPanel('choices_origin'),
        ]),
        MultiFieldPanel([
            FieldPanel('slug'),
            FieldPanel('seo_title'),
            FieldPanel('search_description'),
        ], ugettext_lazy('Common page configuration')),
    ]

    # API
    api_fields = [
        'sidebar_order', 'non_emergency_callout', 'choices_origin',
        'local_header', 'before', 'main', 'sidebar'
    ]
