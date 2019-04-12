from django.shortcuts import render
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from core.models import Member, Entry
from core.serializers import UIDListSerializer, EntrySerializer


class EntryLogCreate(generics.CreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

    def perform_create(self, serializer):
        serializer.save()
        return Response("Successful")


class MemberUIDList(generics.ListAPIView):
    queryset = Member.objects.all().order_by('-join_date')
    serializer_class = UIDListSerializer
