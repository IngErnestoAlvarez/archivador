from os import rename
from os import path
from pathlib import Path

DEST = r"C:\Users\estud\OneDrive\Documentos\Program\destino"

def carpeta(directory):
    p = Path(directory)
    res = []
    for child in p.iterdir():
        if child.is_dir():
            res.append(child.name)
    return res

def carpetas(directory, name):
    if not isinstance(directory, Path):
        p = Path(directory)
    else:
        p = directory
    for child in p.iterdir():
        if child.is_dir() and name in child.name:
            return child
    return p

def cambiarNombre(fileName, cliente, tipo, impuesto, mes, anio):
    nombre = '-'.join([cliente, tipo, impuesto, mes, anio])
    ext = fileName.suffix
    carpeta = carpetas(fileName.parent, cliente)
    path = Path(carpeta, anio)
    if not (path.exists()):
        path.mkdir()
    path = Path(path, mes)
    if not (path.exists()):
        path.mkdir()
    path = Path(path, nombre + ext)
    if not (path.exists()):
        fileName.rename(path)


def mover(old_file, new_folder):
    nombre = Path(new_folder, old_file.name)
    if not nombre.exists():
        old_file.replace(nombre)

def archivos(directory, names, patterns):
    '''directory: str, name:str, patter:str
    directory es el lugar donde se busca los archivos
    name es el string para filtrar los archivos
    pattern es el tipo de archivo que se busca'''
    res = []
    for pattern in patterns:
        filenames = Path(directory).glob(pattern)
        for file in filenames:
            for name in names:
                if name in file.name.lower():
                    res.append(file)
    return res