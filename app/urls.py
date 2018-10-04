# -*- coding: utf-8 -*-
"""
URL conf for app
"""
from django.urls import include, path
from rest_framework import routers

from app.views import index, TodoViewSet

router = routers.SimpleRouter()
router.register(r'todos', TodoViewSet)

app_name = 'app'
urlpatterns = [
    path('', index, name='home'),
    path('api/', include(router.urls)),
]
