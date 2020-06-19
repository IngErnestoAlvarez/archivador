# archivador

Selecciona archivos específicos de una carpeta, los redirecciona y renombra hacia una carpeta de destino.

## Install

  1. Descargar el repositorio en alguna carpeta.
  2. En la carpeta dentro del repositorio, crear una carpeta 'direcciones'
  3. Dentro de direcciones crearemos 2 archivos:
     - DEST.txt
     - ORIGEN.txt
  4. En cada cual guardar la dirección **absoluta** de las carpetas que queremos tener como origen y destino respectivamente.
  5. En la carpeta _destino_ tendrá que haber dos capas de carpetas.
  6. La primera tiene que ser los regimenes con los que se quiere trabajar.
  7. Dentro de estas, una carpeta por cada cliente. ***NADA MAS***
  
  **Opcional** (Si queremos que el programa empiece con el inicio de windows):
  
  1. En el archivo de Sync aparece un texto que dice `"DIRECCION DE PROGRAMA.BAT"`, modificarlo con la
    dirección **absoluta** de *programa.bat* de esta carpeta. (Guardar el archivo)
  2. Apretar las teclas **Windows** + **r** y escribir: `shell:startup`.
  3. Dentro pegar el archivo *Sync*
  4. Reiniciar el equipo, ya se estará ejecutando el programa.

## Extras

### Cerrar el programa

  Si por alguna razón necesitas cerrar el programa tienes que:

  1. Ir al administrador de tareas
  2. Ir a la pestaña de *detalles*.
  3. Buscar algún detalle que diga 'pythonw.exe' y finalizarlo.

### Modificación de listas

  Para modificar cualquiera de las listas, hay que entrar en cualquiera de los siguientes archivos (ventana.py o main.pyw **en modo de edición**) y apareceran listas como las siguientes:

  ```python
DETECTORES = [
    "dj",
    "ticket",
    "afip",
    "f931",
    "reportes",
    "certificado",
    "comprobante"
]
  ```

  En este caso para agregar un elemento, simplemente tienes que agregar una coma al final del último elemento y agregar un elemento en la linea siguiente (**Atención**: Las comillas al inicio de cada linea tienen que estar alineadas).

  ```python
DETECTORES = [
    "dj",
   "ticket",
  "afip",
      "f931",
    "reportes",
    "certificado",
    "comprobante"
]
  ```

  Algo como esto no funcionará.

### Reiniciar programa

  Para reiniciar el programa, primero que nada, y muy importante, cerrarlo como se indica en el inciso al comienzo de esta sección.
  Una vez cerrado, utilizar el metodo que se usa en el apartado para encontrar la carpeta de inicio (**Windows** + **r**, y adentro escribir `shell:startup`) y ejecutar el archivo *Sync*.
