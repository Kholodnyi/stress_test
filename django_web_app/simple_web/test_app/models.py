from __future__ import absolute_import, unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Entry(models.Model):
    text = models.TextField(verbose_name='Some text')
    amount = models.DecimalField(
        max_digits=15, decimal_places=4,
        verbose_name='Amount')

    def __str__(self):
        return f'{self.pk} | {self.text[:10]}...'

    class Meta:
        verbose_name = _('Entry')
        verbose_name_plural = _('Entries')


class UserRequest(models.Model):
    content_type = models.TextField(verbose_name='Content Type')
    user_agent = models.TextField(verbose_name='User Agent')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id} | {self.created}'

    class Meta:
        verbose_name = _('User Request')
        verbose_name_plural = _('User Requests')
