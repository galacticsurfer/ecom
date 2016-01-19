from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django_extensions.db.models import TimeStampedModel

# PS : DO NOT RUN MAKEMIGRATIONS TILL ALL MODELS ARE FINALIZED !!

class Category(TimeStampedModel):
    """ Category Model """
    name = models.CharField(_('name'), max_length=255)
    slug = models.SlugField(_('slug'), unique=True)
    parent = models.ForeignKey('self', blank=True, null=True, default=None)
    is_root = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    image = models.ImageField(upload_to='', default='') # Handle thumbnail image with sorl-thumbnail
    description = models.TextField(blank=True, null=True, default=None)
    page_title = models.Charfield(max_length=255, null=True, blank=True, default=None)
    meta_keywords = models.CharField(_('meta-keywords'), max_length=255, blank=True, null=True, default='')
    meta_description = models.CharField(_('meta-descriptions'), max_length=255, blank=True, null=True, default='')
    include_in_menu = models.BooleanField(_('include-in-navigation-menu'), default=False)



