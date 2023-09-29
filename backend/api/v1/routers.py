from rest_framework.routers import DefaultRouter

from api.v1.contact.views import ContactViewSet, LabelContactsViewSet
from api.v1.contact_label.views import ContactLabelViewSet
from api.v1.label.views import LabelViewSet

router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contacts')
router.register(r'contact-labels', ContactLabelViewSet, basename='contact-labels')
router.register(r'labels', LabelViewSet, basename='labels')
router.register(r'labels/(?P<label_id>\d+)/contacts', LabelContactsViewSet, basename='label-contacts')

urlpatterns = router.urls
