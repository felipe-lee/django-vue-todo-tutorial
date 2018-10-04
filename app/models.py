# -*- coding: utf-8 -*-
"""
Models for app
"""
from __future__ import unicode_literals

from django.db import models


class Todo(models.Model):
    """
    Model to manage to do items.
    """

    text = models.CharField(max_length=200)

    def __str__(self):
        return f'Todo: self.text'
