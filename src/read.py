import pandas as pd

def readFile():
    
    df = pd.read_excel('students.xlsx', sheet_name='asistencias')

    print("""
        INFORMACIÓN
      """)
    
    print(df)

    print()

    print(df.head(5))