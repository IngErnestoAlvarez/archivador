from funciones import cambiarNombre
from funciones import archivos
from funciones import DEST
from funciones import moverABasura
from pathlib import Path
from time import sleep
import tkinter
from ventana import App

'''TODO:
'''

with open(r"direcciones\ORIGEN.txt", 'r', encoding='utf-8') as f:
    ORIGEN = f.readline()

DETECTORES = [
    "dj",
    "ticket",
    "afip",
    "f931",
    "reportes",
    "certificado",
    "comprobante",
    "credencial"
]

TIPOS_ARCHIVOS = [
    "*.*",
    "*."
]

def main():
    while True:
        arch = archivos(ORIGEN, DETECTORES, TIPOS_ARCHIVOS)
        for file in arch:
            app = App(file.stem)
            app.mainloop()
            if app.cerrado:
                cambiarNombre(file,app.nombre.get(),app.cliente.get(),app.tipo.get(), app.impuesto.get(), app.mes.get(),app.anio.get())
            else:
                moverABasura(file, ORIGEN)
        sleep(5)

if __name__ == "__main__":
    main()
