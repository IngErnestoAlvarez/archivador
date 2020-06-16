import tkinter as tk
from tkinter import ttk
from functools import partial
from tkinter import font
from funciones import DEST
from funciones import carpeta
from datetime import date
# pylint: disable=E1120

NOMBRES_DE_ARCHIVOS = [
    "DDJJ",
    "Ticket",
    "Certificado"
]
IMPUESTOS = [
    "IVA",
    "IIBB",
    "CM",
    "Ganancias",
    "BP",
    "Citi Compras y ventas",
    "931",
    "Participaciones societarias",
    "Certif. PyMe",
    "Extención ganancias",
    "Otros"
]
MESES = [
    "ENE",
    "FEB",
    "MAR",
    "ABR",
    "MAY",
    "JUN",
    "JUL",
    "AGO",
    "SEP",
    "OCT",
    "NOV",
    "DIC",
    "ANUAL"
]

ANIOS = [str(x) for x in range(date.today().year-5, date.today().year+1)]

def terminar(app):
    if app.nombre.get() != 'Cliente':
        app.cerrado = True
    app.root.destroy()


def mesAnterior(mes):
    if(mes == 1):
        return 12
    return mes-1

def crearStringVar(root, seteado):
    aux = tk.StringVar(root)
    aux.set(seteado)
    return aux

class App(tk.Frame):
    def __init__(self, filename):
        self.root = tk.Tk(screenName="Archivo")
        self.root.title(filename)
        self.root.resizable(width=False, height=False)
        super(App, self).__init__(self.root)
        self.root.geometry("300x350")
        self.root["bg"] = "#1DB954"
        self.nombre = crearStringVar(self.root, 'Cliente')
        self.mes = crearStringVar(self.root, MESES[mesAnterior(date.today().month)-1])
        self.anio = crearStringVar(self.root, '2020')
        self.tipo = crearStringVar(self.root, 'Tipo')
        self.impuesto = crearStringVar(self.root, 'Impuesto')
        self.cerrado = False
        self.doWindow()

    def doWindow(self):
        fontExample = font.Font(root=self.root,family="Bahnschrift SemiBold", size=12)

        self.menu = tk.OptionMenu(self.root, self.nombre, *(carpeta(DEST)))
        self.menu.pack(fill=tk.Y,pady=5)
        self.menu['font'] = fontExample
        self.menu['bg'] = "#FFFFFF"

        self.textTipo = tk.OptionMenu(self.root, self.tipo, *NOMBRES_DE_ARCHIVOS)
        self.textTipo.pack(fill=tk.Y,pady=5)
        self.textTipo['font'] = fontExample
        self.textTipo['bg'] = "#FFFFFF"

        self.textImpuesto = tk.OptionMenu(self.root, self.impuesto, *IMPUESTOS)
        self.textImpuesto.pack(fill=tk.Y,pady=5)
        self.textImpuesto['font'] = fontExample
        self.textImpuesto['bg'] = "#FFFFFF"

        self.textMes = tk.OptionMenu(self.root, self.mes,*MESES)
        self.textMes.pack(fill=tk.Y,pady=5)
        self.textMes['font'] = fontExample
        self.textMes['bg'] = "#FFFFFF"

        self.textAnio = tk.OptionMenu(self.root,self.anio, *ANIOS)
        self.textAnio.pack(fill=tk.Y,pady=5)
        self.textAnio['font'] = fontExample
        self.textAnio['bg'] = "#FFFFFF"


        self.button = tk.Button(self.root, text="Terminar",command= lambda: terminar(self))
        self.button.pack(fill=tk.Y,pady=35)
        self.button['bg'] = "#E1E8ED"
        self.button['font'] = fontExample




