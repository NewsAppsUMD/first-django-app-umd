import csv
from expenses.models import Detail
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def handle(self, *args, **options):
        print("Loading CSV")
        csv_path = "./detail.csv"
        csv_file = open(csv_path, 'r')
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            obj = Detail.objects.create(
                bioguide_id=row['BIOGUIDE_ID'],
                office=row['OFFICE'],
                quarter=row['QUARTER'],
                program=row['PROGRAM'],
                category=row['CATEGORY'],
                sort_sequence=row['SORT SEQUENCE'],
                date=row['DATE'],
                transcode=row['TRANSCODE'],
                recordid=row['RECORDID'],
                payee=row['PAYEE'],
                start_date=row['START DATE'],
                end_date=row['END DATE'],
                purpose=row['PURPOSE'],
                amount=row['AMOUNT'],
                year=row['YEAR']
            )
            print(obj)
