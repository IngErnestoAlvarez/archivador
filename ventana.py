import tkinter as tk
from tkinter import ttk
from functools import partial
from tkinter import font
from funciones import DEST
from funciones import carpeta


def terminar(app):
    app.nombre = app.cliente.get()
    app.mes = app.textMes.get()
    app.anio = app.textAnio.get()
    app.tipo = app.textTipo.get()
    app.root.destroy()



class App(tk.Frame):
    def __init__(self, filename):
        self.root = tk.Tk(screenName="Archivo")
        self.root.title(filename)
        self.root.resizable(width=False, height=False)
        super(App, self).__init__(self.root)
        self.root.geometry("300x200")
        self.root["bg"] = "#1DB954"
        self.doWindow()
        self.nombre = ""
        self.mes = 0
        self.anio = 1998
        self.tipo = "DDJJ"

    def doWindow(self):
        fontExample = font.Font(root=self.root,family="Bahnschrift SemiBold", size=12)
        self.widgets = {}

        self.cliente = tk.StringVar(self.root)
        self.cliente.set('Cliente')

        self.menu = tk.OptionMenu(self.root, self.cliente, *(carpeta(DEST)))
        self.menu.pack(fill=tk.Y,pady=5)
        self.menu['font'] = fontExample
        self.menu['bg'] = "#FFFFFF"

        self.textTipo = tk.Entry(self.root, width=30)
        self.widgets['Tipo'] = self.textTipo
        self.textMes = tk.Entry(self.root,  width=30)
        self.widgets['Mes'] = self.textMes
        self.textAnio = tk.Entry(self.root,  width=30)
        self.widgets['Año'] = self.textAnio

        for name,wid in self.widgets.items():
            wid.insert(tk.INSERT,name)
            wid.pack(fill=tk.Y,pady=5)
            wid['font'] = fontExample

        self.button = tk.Button(self.root, text="Terminar",command= lambda: terminar(self))
        self.button.pack(fill=tk.Y,pady=10)
        self.button['bg'] = "#E1E8ED"
        self.button['font'] = fontExample




