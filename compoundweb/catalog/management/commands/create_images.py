import csv
from django.core.management import BaseCommand
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import AllChem
import os
from pathlib import Path
#
# script_dir = os.path.dirname(os.path.realpath('__file__'))
# d = Path().resolve().parent.parent
# with open("data.csv", 'rt', encoding='utf-8') as f:
#     reader = csv.reader(f, dialect='excel', delimiter=",")
#     next(reader, None)
#     for row in reader:
#          # print(row)
#         m = Chem.MolFromSmiles(row[1])
#         print(m)
#         rel_path = "/static/catalog/media/picture/"+row[2]+".png"
#         filename= os.path.join(d, rel_path)
#         print(filename)
#         Draw.MolToFile(m, filename)




# m = Chem.MolFromSmiles('Cc1ccccc1')
# tmp=AllChem.Compute2DCoords(m)
# Draw.MolToFile(m,'cdk2_mol1.o.png')
class Command(BaseCommand):
    help = 'Load a questions csv file into the database'




    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        # d = Path().resolve().parent.parent
        script_dir = os.path.dirname(os.path.realpath('__file__'))

        # print(script_dir)
        with open(path, 'rt', encoding='utf-8') as f:
            reader = csv.reader(f,dialect='excel',delimiter=",")
            next(reader, None)
            for row in reader:
                # print(row)
                m = Chem.MolFromSmiles(row[1])
                print(m)
                rel_path = "/catalog/static/catalog/media/" + row[2] + ".png"
                filename = script_dir + rel_path
                print(filename)
                Draw.MolToFile(m, filename)
