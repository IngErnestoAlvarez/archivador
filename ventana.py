import tkinter as tk
from tkinter import ttk
from functools import partial
from tkinter import font
from funciones import DEST
from funciones import carpeta
from funciones import clientesIn
from datetime import date
# pylint: disable=E1120

NOMBRES_DE_ARCHIVOS = [
    "DDJJ",
    "Ticket",
    "Certificado",
    "Pago",
    "Compensación",
    "Plan de pago",
    "Papel de Trabajo"
]
NOMBRES_DE_ARCHIVOS.sort()
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
    "Mis facilidades",
    "Moratoria",
    "Policia laboral",
    "Sindical"
]
IMPUESTOS.sort()
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
    if app.cliente.get() != 'Cliente':
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
        self.root.geometry("300x400")
        self.root["bg"] = "#1DB954"
        self.nombre = crearStringVar(self.root, 'Regimen')
        self.mes = crearStringVar(self.root, MESES[mesAnterior(date.today().month)-1])
        self.anio = crearStringVar(self.root, '2020')
        self.tipo = crearStringVar(self.root, 'Tipo')
        self.impuesto = crearStringVar(self.root, 'Impuesto')
        self.cliente = crearStringVar(self.root, 'Cliente')
        self.cerrado = False
        self.doWindow()

    def makeStyle(self, objeto):
        fontExample = font.Font(root=self.root,family="Bahnschrift SemiBold", size=12)
        objeto.pack(fill=tk.Y,pady=5)
        objeto['font'] = fontExample
        objeto['bg'] = "#FFFFFF"

    def makeStyleButton(self, button):
        fontExample = font.Font(root=self.root,family="Bahnschrift SemiBold", size=12)
        button.pack(fill=tk.Y,pady=35)
        button['bg'] = "#E1E8ED"
        button['font'] = fontExample

    def doWindow(self):

        self.listaActual = clientesIn(DEST, self.nombre)
        self.listaActual.sort()

        self.menu = tk.OptionMenu(self.root, self.nombre, *(carpeta(DEST)), command=self.modificarLista)
        self.makeStyle(self.menu)

        self.lista = tk.OptionMenu(self.root, self.cliente, *(self.listaActual))
        self.makeStyle(self.lista)

        self.textTipo = tk.OptionMenu(self.root, self.tipo, *NOMBRES_DE_ARCHIVOS)
        self.makeStyle(self.textTipo)

        self.textImpuesto = tk.OptionMenu(self.root, self.impuesto, *IMPUESTOS)
        self.makeStyle(self.textImpuesto)

        self.textMes = tk.OptionMenu(self.root, self.mes,*MESES)
        self.makeStyle(self.textMes)

        self.textAnio = tk.OptionMenu(self.root,self.anio, *ANIOS)
        self.makeStyle(self.textAnio)

        self.button = tk.Button(self.root, text="Terminar",command= lambda: terminar(self))
        self.makeStyleButton(self.button)

    def modificarLista(self, nombre):
        self.listaActual = clientesIn(DEST, nombre)
        self.listaActual.sort()
        self.lista['menu'].delete(0, 'end')
        for item in self.listaActual:
            self.lista['menu'].add_command(label=item, command=tk._setit(self.cliente, item))



