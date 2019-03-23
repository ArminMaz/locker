from django.conf.urls import url
from .views import SerialConnenction, MemberUIDList, MemberCreate, MemberEntryList

urlpatterns = [
    url(r'^serial/$', SerialConnenction.as_view()),
    url(r'^update/$', MemberUIDList.as_view()),
    url(r'^sign-up/$', MemberCreate.as_view()),
    url(r'^members-entry-details/$', MemberEntryList.as_view())
]
