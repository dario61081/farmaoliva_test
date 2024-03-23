__version__ = "1.0"
__author__ = "Dario Garcia"

import deprecated
from backports.functools_lru_cache import lru_cache


class Area:

    def __init__(self, *, codigo_area: int, nombre_area: str, cantidad_funcionarios: int = 1):
        """
        Nodo del organigrama, actua como area dentro de la organizacion
        :param codigo_area: codigo del area
        :param nombre_area: nombre del area
        :param cantidad_funcionarios: cantidad de funcionarios
        """
        self._codigo_area = codigo_area
        self._nombre_area = str(nombre_area).capitalize()
        self._cantidad_funcionarios = cantidad_funcionarios

        # gestion de jerarquia
        self.parent = None
        self.childs: list[Area] = []

    def get_parent(self):
        """
        Retorna area padre
        :return: Area
        """
        return self.parent

    def get_childs(self):
        """
        Retornar areas hijas
        :return: list[Area]
        """
        return self.childs

    def add_child(self, new_area) -> None:
        """
        Agregar area hija
        :param new_area:
        :return:
        """
        self.childs.append(new_area)

    @deprecated.deprecated
    def agregar_area_hija(self, nueva_area_hija):
        """
        Registrar un area hija
        :param nueva_area_hija: objeto area
        :return:
        """
        if not isinstance(nueva_area_hija, (Area,)):
            raise Exception("Nodo a insertar no es valido")

        nueva_area_hija.padre = self
        self.add_child(nueva_area_hija)

        return nueva_area_hija

    @deprecated.deprecated
    def nivel_jerarquia(self):
        salto = 0
        padre = self.get_parent()
        while padre:
            salto += 1
            padre = padre.get_parent()

        return salto

    @deprecated.deprecated
    def imprimir_jerarquia(self):
        """
        Obtener nivel de jerarquia en el arbol
        :return: (int)
        """
        print(self)
        for i in self.get_childs():
            i.imprimir_jerarquia()

    @lru_cache(maxsize=100)
    def get(self, codigo):
        """
        Obtener el area instanciada usando su codigo
        :param codigo: codigo del area
        :return: instancia del area
        """

        if self._codigo_area == codigo:
            return self

        if self.get_childs():
            for h in self.get_childs():
                f = h.get(codigo)
                if f:
                    # f.imprimir()  # depuracion
                    return f
        return None

    @lru_cache(maxsize=10)
    def get_cantidades_funcionarios(self):
        """
        Funcion que retorna la cantidad de funcionarios afectados en la rama
        """
        # sumador...
        suma = 0
        # sumar del nodo actual
        suma += self._cantidad_funcionarios

        # si hay hijas sumar
        if self.get_childs():
            for h in self.get_childs():
                suma += h.get_cantidades_funcionarios()

        return suma

    def __str__(self):
        marca = " " * self.nivel_jerarquia() * 2 + "+" if self.parent else " "
        return "{marca} [{codigo}] {nombre} (funcionarios: {cantidad} [{total}]) " \
            .format(marca=marca,
                    nombre=self._nombre_area,
                    cantidad=self._cantidad_funcionarios,
                    codigo=self._codigo_area,
                    total=self.get_cantidades_funcionarios() or 0
                    )

    @lru_cache(maxsize=10)
    def borrar_area(self, codigo):
        if self.get_childs():
            for h in self.get_childs():
                if h._codigo_area == codigo:
                    del h
                    return True
                else:
                    h.borrar_area(codigo)

        if self.nivel_jerarquia() == 0:
            return False

    @lru_cache(maxsize=100)
    def sumorg(self, codigo_padre):
        suma = 0
        if self.get_childs():
            for h in self.get_childs():
                suma += h.sumorg(codigo_padre)

        suma += self._cantidad_funcionarios
        return suma

    @lru_cache(maxsize=100)
    def find(self, codigo_area):
        if self._codigo_area == codigo_area:
            return self
        else:
            if self.get_childs():
                for h in self.get_childs():
                    f = h.find(codigo_area)
                    if f:
                        return f
