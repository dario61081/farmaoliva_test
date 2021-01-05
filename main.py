__version__ = "1.0"
__author__ = "Dario Garcia"

import os

from entidades import *


def sumorg(organigrama, codigo_nodo):
    """
    Funcion para hacer conteo de cantidad de funcionarios por nodos de una jerarquia
    :return:
    """
    if not isinstance(organigrama, (Organigrama,)):
        raise Exception("El organigrama a procesar no es un objeto valido")
    if not isinstance(codigo_nodo, (int,)):
        raise Exception("Codigo de nodo no es numerico")

    r = organigrama.get_area(codigo_nodo)
    return r.raiz.get_cantidades_funcionarios() or 0


if __name__ == '__main__':
    # creacion del organigrama
    # raiz = Area(1, "gerencia", 3)
    # raiz.agregar_area_hija(Area(6, "contabilidad", 10))
    #
    # factu = raiz.agregar_area_hija(Area(8, "facturacion", 4))
    # factu.agregar_area_hija(Area(9, "Informatica", 4))
    # factu.agregar_area_hija(Area(2, "Clientes", 3))
    #
    # raiz.agregar_area_hija(Area(4, "tesoreria", 6))

    # instanciacion del organigrama
    filename = os.path.join(os.path.dirname(__file__), 'organigrama.json')
    z = Organigrama("Ejemplo 1")
    z.cargar_archivo(filename=filename)
    # z.raiz = raiz
    # impresion del organigrama
    z.imprimir_organigrama()

    # resultados...
    # print sumorg(z, 8)
    # print sumorg(z, 1)
    # print sumorg(z, 4)
