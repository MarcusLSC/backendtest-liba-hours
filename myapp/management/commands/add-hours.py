from django.core.management.base import BaseCommand
from myapp.models import OpeningHours

class Command(BaseCommand):
    help = 'Add opening hours to the database'

    def handle(self, *args, **kwargs):
        OpeningHours.objects.create(day_of_week='Thursday', venue='G/F Entrance', opening_time='09:00 - 17:00')
        OpeningHours.objects.create(day_of_week='Thursday', venue='Learning Commons', opening_time='24 Hours')
        OpeningHours.objects.create(day_of_week='Thursday', venue='LG5 Entrance', opening_time='3:00pm - 11:00pm')
        self.stdout.write(self.style.SUCCESS('Successfully added opening hours'))