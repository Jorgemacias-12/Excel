import pandas as pd

def updateInfo():
    
    df = pd.read_excel('students.xlsx', sheet_name='asistencias')

    df.at[2, 'Nombre'] = "Josue"

    df.to_excel('students.xlsx', sheet_name='asistencias', index=False)