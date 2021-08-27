from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

# Create your models here.

class ServiceListingPage(Page):
    template = "services/service_listing_page.html"
    subtitle = models.TextField(blank=True,
    max_length=500,)

    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
    ]
# add context 
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context['services'] = ServicePage.objects.live().public()

        return context


class ServicePage(Page):
    template = "services/service_page.html"
    description = models.TextField(
        blank=True,
        max_length=500)
    internal_page=models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name='+',
        help_text='select internal page',
        on_delete=models.SET_NULL,
    )
    external_page= models.URLField(blank=True)
    button_text=models.CharField(max_length=50,blank=True)
    service_image= models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        help_text='This image will be used on service listing page and cropped to 570px by 370px',
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        PageChooserPanel('internal_page'),
        FieldPanel('external_page'),
        FieldPanel('button_text'),
        ImageChooserPanel('service_image'),
    ]
