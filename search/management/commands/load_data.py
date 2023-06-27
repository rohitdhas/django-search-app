import csv
from django.core.management.base import BaseCommand
from search.models import Restaurant

class Command(BaseCommand):
    help = 'Loads data from CSV file into the database'

    def handle(self, *args, **options):
        Restaurant.objects.all().delete()  # Clear the table

        with open('data/data.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                dish = Restaurant(
                    name=row['name'],
                    location=row['location'],
                    menu=row['items']
                )
                dish.save()

        self.stdout.write(self.style.SUCCESS('Data loaded successfully.'))
