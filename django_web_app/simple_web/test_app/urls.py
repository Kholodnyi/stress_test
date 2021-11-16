from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EntryViewSet, WriteView

router = DefaultRouter()
router.register(r'entries', EntryViewSet, 'entry')

urlpatterns = [
    path('', include(router.urls)),

    path('user_request/', WriteView.as_view(), name='write_in_db'),
]
