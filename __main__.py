from src.create import createFile, insertStudent
from src.read import readFile
from src.update import updateInfo

def menu():
    
    print("Opciones: ")
    print("""

      1. Crear archivo / Insertar información en archivo
      2. Leer información
      3. Actualizar información ""
      4. Eliminar información

    """)

    option = int(input("==>  "))

    if option == 1:

      createFile()
      insertStudent()

      pass
    if option == 2:

      readFile()

      pass
    if option == 3:
      
      updateInfo()

      pass
    if option == 4:
      pass


    pass

if __name__ == "__main__":
    
    menu()

    pass