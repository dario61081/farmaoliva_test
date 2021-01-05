__version__ = "1.0"
__author__ = "Dario Garcia"
__all__ = ["Area"]

from backports.functools_lru_cache import lru_cache


class Area:

    def __init__(self, codigo, nombre, cantidad):
        """
        Nodo del organigrama, actua como area dentro de la organizacion
        :param codigo: codigo del area
        :param nombre: nombre del area
        :param cantidad: cantidad de funcionarios
        """
        self.codigo = codigo
        self.nombre = str(nombre).capitalize()
        self.cantidad = cantidad
        self.areas_hijas = []
        self.padre = None

    def agregar_area_hija(self, nueva_area_hija):
        """
        Registrar un area hija
        :param nueva_area_hija: objeto area
        :return:
        """
        if not isinstance(nueva_area_hija, (Area,)):
            raise Exception("Nodo a insertar no es valido")

        nueva_area_hija.padre = self
        self.areas_hijas.append(nueva_area_hija)

        return nueva_area_hija

    def jerarquia(self):
        salto = 0
        padre = self.padre
        while padre:
            salto += 1
            padre = padre.padre

        return salto

    def imprimir_jerarquia(self):
        print(self)
        if self.areas_hijas:
            for i in self.areas_hijas:
                i.imprimir_jerarquia()

    def get(self, codigo):
        """
        Obtener el area instanciada usando su codigo
        :param codigo: codigo del area
        :return: instancia del area
        """

        if self.codigo == codigo:
            # self.imprimir()  # depuracion
            return self
        else:
            if self.areas_hijas:
                for h in self.areas_hijas:
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

        # si hay hijas sumar
        if self.areas_hijas:
            for h in self.areas_hijas:
                suma += h.get_cantidades_funcionarios()

        # sumar del nodo actual
        suma += self.cantidad

        return suma

    def __str__(self):
        marca = " " * self.jerarquia() * 2 + "+" if self.padre else " "
        return "{marca} {nombre} ({cantidad}) [{codigo}]" \
            .format(marca=marca,
                    nombre=self.nombre,
                    cantidad=self.cantidad,
                    codigo=self.codigo
                    )
