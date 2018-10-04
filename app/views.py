# -*- coding: utf-8 -*-
"""
Views for app
"""
from typing import Type, Union, List

from django.db.models import QuerySet
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action

from app.models import Todo
from app.serializers import TodoSerializer


def index(request: HttpRequest) -> HttpResponse:
    """
    Renders landing page.

    Args:
        request: user request

    Returns:
        index

    """
    return render(request, 'index.html')


class TodoViewSet(viewsets.ModelViewSet):
    """
    Viewset for T odo model
    """
    queryset: Union[QuerySet, List[Todo]] = Todo.objects.all()
    serializer_class: Type[TodoSerializer] = TodoSerializer

    @action(methods=['delete'], detail=False)
    def clear_todos(self, request: HttpRequest) -> HttpResponse:
        """
        Deletes all existing T odo instances.

        Args:
            request: user request

        Returns:
            successful response

        """
        todos = Todo.objects.all()
        todos.delete()
        return HttpResponse(status=200)
