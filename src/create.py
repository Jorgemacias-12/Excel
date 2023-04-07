# import openpyxl
from openpyxl import Workbook
import os

def createFile():
    
    fileName = input('Nombre de archivo: ')

    workbook = Workbook()

    workbook.save(fileName + ".xlsx")