from hashlib import sha512
from typing import Protocol

from entidades import Organigrama, Area


class IOrganigramaAction(Protocol):
    def __call__(self, organigrama: Organigrama, **kwargs) -> None:
        pass


class IStateAction(Protocol):
    def __call__(self, prior_state: bool) -> bool:
        pass


class ActionOrganigramaAddArea(IOrganigramaAction):

    def __call__(self, organigrama: Organigrama, **kwargs) -> None:

        cursor = "[CREAR] {}> "
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
                # area.agregar_area_hija(nueva_area)
                organigrama.create_area(area=nueva_area, parent=area)
            print("Agregado al area {}".format(codigo_area))


class ActionOrganigramaRemoveArea(IOrganigramaAction):
    def __call__(self, organigrama: Organigrama, **kwargs) -> None:
        cursor = "[ELIMINAR]: {}> "

        root = organigrama.get_root()
        if not root:
            print("(!) El organigrama no tiene areas definidas")
            return

        codigo = int(input(cursor.format("Codigo del area a borrar")))

        area = root.find(codigo)
        if area:
            print("Area encontrada")
        else:
            print("Area no encontrada")


class ActionOrganigramaRender(IOrganigramaAction):
    def __call__(self, organigrama: Organigrama, **kwargs) -> None:
        organigrama.render()


class ActionOrganigramaTotalizar(IOrganigramaAction):
    def __call__(self, organigrama: Organigrama, **kwargs) -> None:
        root = organigrama.get_root()
        if not root:
            print("(!) El organigrama no tiene areas definidas")
            return

        print("La cantidad total de funcionarios es: {}".format(root.get_cantidades_funcionarios()))

        # print("La cantidad total de funcionarios es: {}".format(organigrama.get_root().sumorg(1)))


class ActionOrganigramaExport(IOrganigramaAction):
    def __call__(self, organigrama: Organigrama, **kwargs) -> None:
        import os
        folder = os.path.join(os.getcwd(), "files")
        if not os.path.exists(folder):
            os.mkdir(folder)

        tempname = lambda: sha512(os.urandom(64)).hexdigest()[:8]
        name = input("Nombre del archivo > ") or tempname()

        filename = os.path.join(folder, name)
        print("Guardando organigrama en {}".format(filename))
        with open(filename, "w") as f:
            f.write(organigrama.__str__())


class ActionOrganigramaImport(IOrganigramaAction):
    def __call__(self, organigrama: Organigrama, **kwargs) -> None:
        filename = input("Nombre del archivo > ")
        print("Cargando organigrama desde {}".format(filename))
