from funciones import cambiarNombre
from funciones import mover
from funciones import archivos
from funciones import DEST
from pathlib import Path
from time import sleep
import tkinter
from ventana import App

ORIGEN = r"C:\Users\estud\OneDrive\Documentos\Program\origen"

DETECTORES = [
    "PDJ"
]

TIPOS_ARCHIVOS = [
    "*.txt",
    "*.pdf"
]

def main():
    while True:
        arch = archivos(ORIGEN, DETECTORES, TIPOS_ARCHIVOS)
        for file in arch:
            mover(file, DEST)
        arch = archivos(DEST, DETECTORES, TIPOS_ARCHIVOS)
        for file in arch:
            app = App(file.stem)
            app.mainloop()
            cambiarNombre(file,app.nombre.get(),app.tipo.get(),app.mes.get(),app.anio.get())
        sleep(5)

if __name__ == "__main__":
    main()