#Import de arquivos
import pandas

from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filename = askopenfilename()

# Carrega os Dados
url = pandas.ExcelFile(filename)
names = ['POINT-INDEX', 'EQUIPAMENTO', 'IO']
dataset = pandas.read_excel(url, sheet_name='Configuração', names=names, usecols='H,I,J')
datasets = dataset.drop(dataset[dataset['POINT-INDEX'] == 0].index)
print(datasets)
