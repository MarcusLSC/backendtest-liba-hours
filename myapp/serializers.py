from rest_framework import serializers

from .models import OpeningHours

class OpeningHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHours
        fields = ['day_of_week', 'venue', 'opening_time']