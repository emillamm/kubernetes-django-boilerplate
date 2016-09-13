from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from markdownx.models import MarkdownxField
from django.utils import timezone
from django.template.defaultfilters import slugify

import uuid


class BlogPost(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    posted_at = models.DateTimeField()
    title = models.CharField(max_length=500)
    body = MarkdownxField(null=True, blank=True)
    excerpt = MarkdownxField(null=True, blank=True)
    slug = models.SlugField(max_length=60, blank=True, unique=True)
    draft = models.BooleanField(default=True)

    class Meta:
        pass


@receiver(pre_save, sender=BlogPost)
def blogpost_init_fields(sender, instance, raw, **kwargs):
    if not instance.posted_at:
        instance.posted_at = timezone.now()
    if not instance.slug:
        if instance.title:
            instance.slug = slugify(instance.title)
        else:
            instance.slug = str(uuid.uuid4())
