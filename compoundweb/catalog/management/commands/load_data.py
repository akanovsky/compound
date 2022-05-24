import csv
from django.core.management import BaseCommand
from catalog.models import Compound,Library

class Command(BaseCommand):
    help = 'Load a questions csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        with open(path, 'rt', encoding='utf-8') as f:
            reader = csv.reader(f,dialect='excel',delimiter=",")
            next(reader, None)
            temp=[]
            for row in reader:
                Compound.objects.create(
                    name=row[0],
                    smiles=row[1],
                    inchlkey=row[2],
                    c_set=row[3]
                )
                if row[3] not in temp:
                    Library.objects.create(
                        name=row[3]
                    )
                    temp.append(row[3])
