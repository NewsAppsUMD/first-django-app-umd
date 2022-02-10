import csv
from expenses.models import Summary
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Loading CSV")
        csv_path = "./summary.csv"
        csv_file = open(csv_path, 'r')
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            obj = Summary.objects.create(
                bioguide_id=row['BIOGUIDE_ID'],
                office=row['OFFICE'],
                program=row['PROGRAM'],
                category=row['CATEGORY'],
                year_to_date=row['YTD'],
                amount=row['AMOUNT'],
                year=row['YEAR'],
                quarter=row['QUARTER']
            )
            print(obj)
