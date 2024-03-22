__version__ = "1.0"
__author__ = "Dario Garcia"
__celular__ = "0985830541"
__email__ = "dario61081@gmail.com"

from entidades import *
from funciones.organigrama_funciones import leer_y_cargar_organigrama, sumorg


def main():
     # ejecutar rutinas de carga y acciones
    titulo = input("Titulo del organigrama > ")
    if not titulo:
        titulo = "Empresa ABC"

    organigrama = leer_y_cargar_organigrama(Organigrama(titulo))

    if organigrama:

        cursor = "{} > "
        lectura = True
        FIN_LOOP = -1

        while lectura:
            organigrama.imprimir_organigrama()

            try:
                codigo_area = int(input(cursor.format("Codigo del area a ejecutar sumorg(?) | {}: Salir ".format(FIN_LOOP))))
                if codigo_area:
                    if codigo_area == FIN_LOOP:
                        lectura = False
                    else:
                        valor = sumorg(organigrama, codigo_area)
                        print ("sumorg({},{}) = {}".format(organigrama.titulo, codigo_area, valor))
            except Exception as e:
                """
                Capturar errores de inputs o conversion
                """
                print("(!) {}".format(e))

if __name__ == '__main__':
    main()
