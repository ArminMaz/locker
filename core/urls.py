from django.conf.urls import url
from .views import MemberUIDList, EntryLogCreate

urlpatterns = [
    url(r'^entry-log/$', EntryLogCreate.as_view()),
    url(r'^members-list/$', MemberUIDList.as_view()),
]
