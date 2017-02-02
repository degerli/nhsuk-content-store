from ..blocks import StreamBlock, StructBlock
from .base import Component
from .text import text


class PanelBlock(StructBlock):
    header = StreamBlock([
        text.as_tuple()
    ])

    body = StreamBlock([
        text.as_tuple()
    ])

    footer = StreamBlock([
        text.as_tuple()
    ])


panel = Component('panel', PanelBlock(icon="radio-full"))
