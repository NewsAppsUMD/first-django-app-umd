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
                date=row.get('DATE') or None,
                transcode=row['TRANSCODE'],
                recordid=row['RECORDID'].strip(),
                payee=row['PAYEE'],
                start_date=row.get('START DATE') or None,
                end_date=row.get('END DATE') or None,
                purpose=row['PURPOSE'],
                amount=row['AMOUNT'],
                year=row['YEAR']
            )
            print(obj)
