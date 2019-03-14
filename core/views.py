from django.shortcuts import render
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from core.models import Member
from core.serializers import MemberCreateSerializer, UIDListSerializer


class SerialConnenction(APIView):
    def post(self, request):
        serial = self.request.data.get('serial')
        print(serial)
        return Response('Serial Uploaded Successfully.')


class MemberCreate(generics.CreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberCreateSerializer

    def perform_create(self, serializer):
        serializer.save()


class MemberUIDList(generics.ListAPIView):
    queryset = Member.objects.all()
    serializer_class = UIDListSerializer
