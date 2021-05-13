from django.db import models
from django.db.models.base import Model


class IndexPage(models.Model):
    title = models.CharField('Title of Endpoint', max_length=100)
    url = models.URLField('URL of the Endpoint', max_length=200)
    has_get = models.BooleanField('GET')
    has_post = models.BooleanField('POST')
    has_put = models.BooleanField('PUT')
    has_patch = models.BooleanField('PATCH')
    has_delete = models.BooleanField('DELETE')

    def __str__(self):
        return self.title


class AboutPage(models.Model):
    heading = models.CharField('About page Heading', max_length=100)
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.heading
