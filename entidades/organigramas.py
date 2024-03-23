__version__ = "1.0"
__author__ = "Dario Garcia"
__all__ = ['Organigrama']

from entidades import Area


class Organigrama:
    """
    Clase para manejo de un organigrama
    """

    def __init__(self, *, titulo: str):
        """
        Constructor organigrama
        :param nombre: nombre del organigrama
        """
        self._titulo = titulo
        self._raiz = None

    def get_root(self) -> Area:
        """
        Obtener raiz del organigrama
        :return: Area
        """
        return self._raiz

    def render(self) -> None:
        """
        Render del organigrama
        """
        print("\n\n*** Organigrama \"{titulo}\" ***".format(titulo=self._titulo))

        if not self.get_root():
            print("(!) El organigrama no tiene areas definidas, presione a para agregar una")
            return

        self.get_root().imprimir_jerarquia()

    def get_area_by_codigo(self, *, codigo_area: int):
        """
        Obtener el area por medio del codigo de area
        :param codigo_area: codigo (int)
        :return: objeto area relacionado
        """
        if self._raiz:
            return self._raiz.get(codigo_area)

    def create_area(self, *, area: Area, parent: Area = None):
        """
        Agregar area
        :param area:
        :param parent:
        :return:
        """
        if not parent:
            self._raiz = area
        else:
            parent.add_child(area)

    def sumorg(self, codigo_area):
        """
        Devuelve la sumatoria de funcionarios del area y areas relacionadas
        :param codigo_area: codigo del area
        :return: sumatoria de funcionarios (int)
        """
        inicio = self.get_area_by_codigo(codigo_area=codigo_area)
        if inicio:
            return inicio.sumorg()
        else:
            print("Area con el codigo {codigo_area} no existe".format(codigo_area=codigo_area))
            return 0
