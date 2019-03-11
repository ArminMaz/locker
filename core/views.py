from django.shortcuts import render
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response


class SerialConnenction(APIView):
    def post(self, request):
        serial = self.request.data.get('serial')
        print(serial)
        return Response('Serial Uploaded Successfully.')
