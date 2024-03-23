from typing import Protocol

from entidades import Organigrama, Area
from funciones.tools import sumorg


class IOrganigramaAction(Protocol):
    def __call__(self, organigrama: Organigrama, **kwargs) -> None:
        pass


class IStateAction(Protocol):
    def __call__(self, prior_state: bool) -> bool:
        pass


class ActionOrganigramaAddArea(IOrganigramaAction):

    def __call__(self, organigrama: Organigrama, **kwargs) -> None:

        cursor = "[NUEVO] {}> "

        codigo = int(input(cursor.format("Codigo del area")))
        nombre = input(cursor.format("Nombre del area"))
        cantidad = int(input(cursor.format("Cantidad del area")))

        nueva_area = Area(codigo_area=codigo, nombre_area=nombre, cantidad_funcionarios=cantidad)

        if not organigrama.get_root():
            organigrama.create_area(area=nueva_area, parent=None)
            print(f"Agregado area \"{nueva_area.get_title()}\" como raiz del organigrama")
            return

        if organigrama.get_root():
            codigo_area = int(input(cursor.format("Codigo del area padre a asignar")) or 0)
            area = organigrama.get_root().find(codigo_area)
            if area:
                area.agregar_area_hija(nueva_area)
            print("Agregado al area {}".format(codigo_area))


class ActionOrganigramaRemoveArea(IOrganigramaAction):
    def __call__(self, organigrama: Organigrama, **kwargs) -> None:
        cursor = "ELIMINAR: {}> "
        codigo = int(input(cursor.format("Codigo del area a borrar")))
        area = organigrama.get_root().find(codigo)
        if area:
            organigrama.remove_area(area=area)
        else:
            print("Area no encontrada")


class ActionOrganigramaRender(IOrganigramaAction):
    def __call__(self, organigrama: Organigrama, **kwargs) -> None:
        organigrama.render()


class ActionOrganigramaTotalizar(IOrganigramaAction):
    def __call__(self, organigrama: Organigrama, **kwargs) -> None:
        print("La cantidad total de funcionarios es: {}".format(sumorg(organigrama=organigrama, codigo_nodo=0)))
