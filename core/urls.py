from django.conf.urls import url
from .views import SerialConnenction, MemberUIDList

urlpatterns = [
    url(r'^serial/$', SerialConnenction.as_view()),
    url(r'^update/$', MemberUIDList.as_view())
]
