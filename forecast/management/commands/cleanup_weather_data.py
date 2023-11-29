# forecast/management/commands/cleanup_weather_data.py

from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from django.db.models import Q  # Import the Q object
from forecast.models import Weather

class Command(BaseCommand):
    help = 'Deletes weather data older than today'

    def handle(self, *args, **options):
        now = datetime.now()
        today = now.strftime("%Y%m%d")

        # Calculate an hour ago for base_time comparison
        an_hour_ago = (now - timedelta(hours=1)).strftime("%H%M")

        # Delete weather data older than today's base_date or an hour ago's base_time
        Weather.objects.filter(
            Q(base_date__lt=today) | (Q(base_date=today) & Q(base_time__lt=an_hour_ago))
        ).delete()

        self.stdout.write(self.style.SUCCESS('Successfully cleaned up weather data.'))
