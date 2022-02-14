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
            if row['DATE'].strip() == '':
                date = None
            else:
                date = row['DATE']
            if row['START DATE'].strip() == '':
                start_date = None
            else:
                start_date = row['DATE']
            if row['END DATE'].strip() == '':
                end_date = None
            else:
                end_date = row['END DATE']
            obj = Detail.objects.create(
                bioguide_id=row['BIOGUIDE_ID'],
                office=row['OFFICE'],
                quarter=row['QUARTER'],
                program=row['PROGRAM'],
                category=row['CATEGORY'],
                sort_sequence=row['SORT SEQUENCE'],
                date=date,
                transcode=row['TRANSCODE'],
                recordid=row['RECORDID'].strip(),
                payee=row['PAYEE'],
                start_date=start_date,
                end_date=end_date,
                purpose=row['PURPOSE'],
                amount=row['AMOUNT'],
                year=row['YEAR']
            )
            print(obj)
