#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import startfile, path
import subprocess



def apertura(fichero):
    try:
        file = open(fichero) if ".txt" in fichero \
               else open(fichero+".txt")
        raw_data = file.readlines()
        file.close()
    except IOError:
        print("El nombre de fichero que has introducido no se encuentra",
              "en la carpeta C:/Python34 , busca donde lo hayas guardado",
              "y metelo en la carpeta Python34.")
    else:
        clean_data = [raw_data[i][:-1] for i in range(len(raw_data))]
        return clean_data

    
def añadir(fichero, symbolo, nuevo_fichero):
    data = apertura(fichero)
    nuevo = open(nuevo_fichero, "w")
    for line in data:
        if len(line) > 0 :
            if line[-1] == symbolo :
                nuevo.write(line+" ")
            else:
                nuevo.write(line+symbolo+" ")
    nuevo.close()


def main():
    fichero = input("Cual es el nombre del fichero que requiere ser modificado? ")
    symbolo = input("Escriba el symbolo o symbolos que requieren ser añadidos a cada linea : ")
    nuevo_fichero = input("Cual es el nombre del fichero donde desea guardar los resultados? ")
    if ".txt" not in nuevo_fichero:
        nuevo_fichero = nuevo_fichero + ".txt"
    añadir(fichero, symbolo, nuevo_fichero)
    print("\nProceso acabado. Tenga un buen dia.")
    deseo = input("\nDesea ver el fichero corregido? : ")
    startfile(nuevo_fichero) if deseo == "si" else None


if __name__ == "__main__":
    main()
    location = input("\nQuieres abrir la carpeta donde se encuentra el fichero corregido? ")
    subprocess.Popen('explorer "C:\Python34"') if location == "si" else None
    print("Goodbye!")
    
