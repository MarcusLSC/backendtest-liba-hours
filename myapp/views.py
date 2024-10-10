from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import OpeningHours
from .serializers import OpeningHoursSerializer

class OpeningHoursView(APIView):
    def get(self, request):
        opening_hours = OpeningHours.objects.all()
        serializer = OpeningHoursSerializer(opening_hours, many=True)
        return Response(serializer.data)

def hello(request):
    return HttpResponse('Hello')
