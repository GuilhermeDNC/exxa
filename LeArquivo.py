#Import de arquivos
import pandas
import Dicionario as dc

from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
filename = askopenfilename(initialdir = "/",title = "Abrir Tabela de Variáveis",filetypes = (("Arquivo Excel","*.xls"),("Todos os Arquivos","*.*")))

# Carrega os Dados
url = pandas.ExcelFile(filename)
names = ['PASTA', 'DESCRIÇÃO', 'IO']

dataset = pandas.read_excel(url, sheet_name='Configuração', names=names, usecols='A,E,F',skiprows=12)
datasets = dataset[dataset['IO'].notnull()]

pointIndex = datasets['IO'].values.tolist()
equipamento = datasets['PASTA'].values.tolist()
io = datasets['DESCRIÇÃO'].values.tolist()

metodo = ''
metodo += '\tpublic void pointIndex(){\n'

for i in range(0, len(pointIndex)):
    metodo += ('\t\t'+dc.pasta[equipamento[i]]+dc.descricao[io[i]]+dc.io[pointIndex[i]] + ';\n')
metodo += '\t}\n'

sistemaPath = askopenfilename(initialdir = "C:\Java Controls",title = "Abrir arquivo Sistema.java",filetypes = (("Arquivo Java","*.java"),("Todos os Arquivos","*.*")))

f = open(sistemaPath, "r")
contents = f.readlines()
f.close()

linhas = sum(1 for linha in contents)

contents.insert(linhas-1, metodo)

f = open(sistemaPath, "w")
contents = "".join(contents)
f.write(contents)
f.close()


