# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 11:58
from __future__ import unicode_literals

import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20161215_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editorialpage',
            name='main',
            field=wagtail.wagtailcore.fields.StreamField((('markdown', wagtail.wagtailcore.blocks.RichTextBlock(label='markdown')), ('panel', wagtail.wagtailcore.blocks.StructBlock((('main', wagtail.wagtailcore.blocks.RichTextBlock()), ('footer', wagtail.wagtailcore.blocks.RichTextBlock()))))), blank=True, null=True, verbose_name='Main Content'),
        ),
    ]
