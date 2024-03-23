from entidades import Organigrama, Area


def sumorg(organigrama, codigo_nodo):
    """
    Funcion para hacer conteo de cantidad de funcionarios por nodos de una jerarquia
    :return:
    """
    if not isinstance(organigrama, (Organigrama,)):
        raise Exception("El argumento pasado como organigrama no es valido")

    if not isinstance(codigo_nodo, (int,)):
        raise Exception("Codigo de nodo no es numerico")

    r = organigrama.get_area_by_codigo(codigo_area=codigo_nodo)
    if not isinstance(r, (Area,)):
        return 0
    else:
        return r.get_cantidades_funcionarios()
