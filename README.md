# archivador
Selecciona archivos específicos de una carpeta, los redirecciona y renombra hacia una carpeta de destino.


## Install:

  1. Descargar el repositorio en alguna carpeta.
  2. En la carpeta dentro del repositorio, crear una carpeta 'direcciones'
  3. Dentro de direcciones crearemos 2 archivos:
     - DEST.txt
     - ORIGEN.txt
  4. En cada cual guardar la dirección **absoluta** de las carpetas que queremos tener como origen y destino respectivamente.
  5. En la carpeta _destino_ tendrá que haber dos capas de carpetas. 
  6. La primera tiene que ser los regimenes con los que se quiere trabajar.
  7. Dentro de estas, una carpeta por cada cliente. ***NADA MAS***
  
  Opcional (Si queremos que el programa empiece con el inicio de windows):
  
  1. En el archivo de Sync aparece un texto que dice `"DIRECCION DE PROGRAMA.BAT"`, modificarlo con la 
    dirección **absoluta** de *programa.bat* de esta carpeta. (Guardar el archivo)
  2. Apretar las teclas **Windows** + **r** y escribir: `shell:startup`.
  3. Dentro pegar el archivo *Sync*
  4. Reiniciar el equipo, ya se estará ejecutando el programa.
