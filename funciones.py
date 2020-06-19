from os import rename
from os import path
from pathlib import Path
from shutil import move
from makes import *
with open("direcciones\DEST.txt", 'r') as f:
    DEST = f.readline()


def clientesIn(directory, aname):
    name = makeToString(aname)
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
    p = makeToPath(directory)
    res = []
    for child in p.iterdir():
        if child.is_dir():
            res.append(child.name)
    return res

def carpetas(directory, name):
    p = makeToPath(directory)
    for child in p.iterdir():
        if child.is_dir() and name in child.name:
            return child
    return p

def carpetaInterna(DEST, cliente):
    p = Path(DEST)
    for carpeta in p.iterdir():
        if carpeta.is_dir():
            for carp in carpeta.iterdir():
                if cliente in carp.name:
                    p = Path(carpeta, cliente)
                    return p

def cambiarNombre(fileName,regimen,cliente, tipo, impuesto, mes, anio):
    nombre = '-'.join([cliente, tipo, impuesto, mes, anio])
    ext = fileName.suffix
    if regimen != 'Regimen':
        carpeta = carpetas(DEST, regimen)
        path = Path(carpeta, cliente)
    else:
        path = carpetaInterna(DEST, cliente)
    path = Path(path, anio)
    if not (path.exists()):
        path.mkdir()
    path = Path(path, mes)
    if not (path.exists()):
        path.mkdir()
    path = Path(path, nombre + ext)
    if not (path.exists()):
        move(fileName, path)
    else:
        parent = path.parent
        path = noRepetido(parent, nombre, ext)
        move(fileName, path)

def noRepetido(parent, nombre, ext):
    nombreAux = nombre
    contador = 2
    pathAux = Path(parent, nombreAux + ext)
    while True:
        if pathAux.exists():
            nombreAux = nombre + "({})".format(contador)
            pathAux = Path(parent, nombreAux + ext)
            contador += 1
        else:
            return pathAux


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