import random
import string

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin

from .models import Entry, UserRequest
from .serializers import EntrySerializer
from simple_web.mixins import CachedRetrieveMixin


class EntryViewSet(ListModelMixin,
                   CachedRetrieveMixin,
                   GenericViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

    @action(detail=False, methods=['POST'])
    def random(self, *args, **kwargs):
        """Generate random Entry objects if DB they count < 1000"""
        count = Entry.objects.all().count()
        if count < 1000:
            entries_create = []
            for _ in range(1000-count):
                entries_create.append(
                    Entry(
                        text=''.join(random.choices(string.ascii_uppercase, k=10000)),
                        amount=random.random()))
            Entry.objects.bulk_create(entries_create)
            response = {'message': f'{1000-count} Entries created'}
        else:
            response = {'message': 'Entries already exists'}
        return Response(response)

    @action(detail=False, methods=['DELETE'])
    def delete_all(self, *args, **kwargs):
        """Delete all Entry objects"""
        Entry.objects.all().delete()
        return Response({'ok': True})


class WriteView(APIView):
    def post(self, *args, **kwargs):
        """
        Write some data in DB
        """
        obj = UserRequest.objects.create(
            content_type=self.request.content_type,
            user_agent=self.request.META['HTTP_USER_AGENT'])

        return Response({'ok': str(obj),
                         'headers': str(type(obj))})

    def delete(self, *args, **kwargs):
        UserRequest.objects.all().delete()
        return Response({'ok': True})
