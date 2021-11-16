import random

from django.core.cache import cache
from rest_framework.exceptions import NotFound
from rest_framework.response import Response


class CachedRetrieveMixin:
    def retrieve(self, request, *args, **kwargs):
        filters = {self.lookup_field: self.kwargs[self.lookup_field]}
        instance = cache.get(self.kwargs[self.lookup_field])
        if not instance:
            try:
                instance = self.queryset.model.objects.get(**filters)
                cache.add(f'{instance.__class__.__name__}{instance.id}', instance, timeout=get_ttl())
            except self.queryset.model.DoesNotExist:
                raise NotFound()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


def get_ttl() -> int:
    """
    Timeout in seconds for cache TTL for avoiding cache stampede

    :return: seconds for cache record expiration
    """
    return int((4 + random.random()) * 60)
