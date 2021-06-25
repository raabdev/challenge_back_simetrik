from django.shortcuts import render
import pandas as pd
from tablib import Dataset
import threading
from sqlalchemy import create_engine

from import_file.models import Persona


def importar(request):

    def read_file():
        try:
            nuevas_personas = request.FILES['csvfile']
            df = pd.read_csv(nuevas_personas)

            engine = create_engine('postgresql+psycopg2://ivan:210192@localhost:5432/challenge_db')

            df.to_sql(name='import_file_persona', con=engine, if_exists='replace', index_label='id')

        except:
            print("ha ocurrido un error, compruebe formato del archivo.")

    if request.method == 'POST':
        read_file()

    return render(request, 'import.html')
