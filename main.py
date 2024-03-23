__version__ = "1.0"
__author__ = "Dario Garcia"
__celular__ = "0985830541"
__email__ = "dario61081@gmail.com"

from entidades import *
from funciones.controller import ControllerOrganigrama


def main():
    # ejecutar rutinas de carga y acciones
    titulo = input("Titulo del organigrama > ")
    if not titulo:
        titulo = "Empresa ABC DEMO"

    ControllerOrganigrama(organigrama=Organigrama(titulo=titulo))()


if __name__ == '__main__':
    main()
