#
# Project: Jacqueline Taylor & Friends
#
# Created on Mon Aug 23 2021
#
# Filename: models.py
#
# Copyright (c) 2021 Bujisoft
#


from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    # models for db
    lead_text=models.CharField(
        max_length=140, 
        blank=True,
        help_text="Subheading text under the bannern title",
        )
    button=models.ForeignKey(
        'wagtailcore.Page', 
        null=True, 
        blank=True, 
        related_name='+',
        help_text="Select an optional page to link to", 
        on_delete=models.SET_NULL,
        )
    button_text=models.CharField(
        max_length=50,
        default="Read More", 
        blank=False, 
        help_text="Button Text",
        )
    banner_background_image=models.ForeignKey(
        'wagtailimages.Image',
        blank=False, 
        help_text="The banner background image",
        null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        )
# content panels for admin to work with models above as input for data
    content_panels = Page.content_panels + [
        FieldPanel("lead_text"),
        PageChooserPanel("button"),
        FieldPanel("button_text"),
        ImageChooserPanel("banner_background_image"),
    ]