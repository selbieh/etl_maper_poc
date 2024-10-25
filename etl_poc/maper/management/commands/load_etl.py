from django.core.management.base import BaseCommand
import csv
import os
from maper.models import Maper

class Command(BaseCommand):
    help = 'Displays stats related to Article and Comment models'

    def handle(self, *args, **kwargs):
        csv_file_path = 'maper/management/commands/employees.csv'
        with open(csv_file_path, mode='r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                print(row)
                # Create a new Maper instance for each row
                Maper.objects.create(
                    id=row['employee_id'],
                    employee_name=row['employee_name']
                )
            print("Records created successfully!")