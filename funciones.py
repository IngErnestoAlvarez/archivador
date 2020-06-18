from os import rename
from os import path
from pathlib import Path
from shutil import move
with open("direcciones\DEST.txt", 'r') as f:
    DEST = f.readline()

def clientesIn(directory, aname):
    if not isinstance(aname, str):
        name = aname.get()
    else:
        name = aname
    p = Path(directory)
    res = []
    if name == 'Regimen':
        for child in p.iterdir():
            if child.is_dir():
                res = res + carpeta(child)
    else:
        for child in (Path(directory, name)).iterdir():
            if child.is_dir():
                res.append(child.name)
    return res


def carpeta(directory):
    if not isinstance(directory, Path):
        p = Path(directory)
    else:
        p = directory
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

def cambiarNombre(fileName,regimen,cliente, tipo, impuesto, mes, anio):
    nombre = '-'.join([cliente, tipo, impuesto, mes, anio])
    ext = fileName.suffix
    carpeta = carpetas(DEST, regimen)
    path = Path(carpeta, cliente)
    path = Path(path, anio)
    if not (path.exists()):
        path.mkdir()
    path = Path(path, mes)
    if not (path.exists()):
        path.mkdir()
    path = Path(path, nombre + ext)
    if not (path.exists()):
        move(fileName, path)


def mover(old_file, new_folder):
    nombre = Path(new_folder, old_file.name)
    if not nombre.exists():
        move(old_file, nombre)

def moverABasura(old_file, origen):
    destino = Path(origen, 'omitidos')
    if destino.exists():
        mover(old_file, destino)
    else:
       destino.mkdir()
       mover(old_file, destino) 

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