# -*- coding: utf-8 -*-
"""
Serializers for app
"""
from rest_framework import serializers

from app.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    """
    Serializer for T odo model (spaced weirdly on purpose to avoid triggering usual highlighting.
    """

    class Meta:
        """
        Define fields from T odo model to use
        """
        model = Todo
        fields = ('text',)
