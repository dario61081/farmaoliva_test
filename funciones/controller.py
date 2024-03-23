__version__ = "1.0"
__author__ = "Dario Garcia"

from entidades import Organigrama, Area
from funciones.actions import RegisterArea, PrintOrganigrama, IAction, RemoveArea


class ControllerOrganigrama:
    """
    Controlador de organigrama
    """

    def __init__(self, *, organigrama: Organigrama) -> None:
        self.organigrama = organigrama
        self.running = True
        self.cursor = "{} > "
        self.actions = {}

        # def remove_area(organigrama: Organigrama, area: Area) -> None:
        #     organigrama.remove_area(area=area)

        # registrar acciones
        self.add_action("a", RegisterArea)
        self.add_action("b", RemoveArea)
        self.add_action("i", PrintOrganigrama)

    def add_action(self, name: str, action: IAction):
        self.actions[name] = action

    def execute_action(self, name: str, organigrama: Organigrama, **kwargs) -> None:
        self.actions[name]()(organigrama, **kwargs)

    def execute(self) -> None:

        def title(titulo: str, divider: str = "") -> None:
            print(f"{titulo}")
            print(f"{divider * len(titulo)}")

        while self.running:

            # vista previa
            # self.organigrama.render()
            self.execute_action("i", self.organigrama, None)
            # seleccione accion?
            comando = input(self.cursor.format("Accion: (a: nuevo | b: borrar | i: imprimir | x: salir "))
            self.execute_action(comando, self.organigrama, None)
            if comando in ('a', 'b', 'i', 'x'):
                if comando == 'a':
                    # agregar nodo

                    print("[Agregar nueva area]")
                    print("-" * 50)
                    codigo = int(input(self.cursor.format("Codigo del area")))
                    nombre = input(self.cursor.format("Nombre del area"))
                    cantidad = int(input(self.cursor.format("Cantidad del area")))

                    nueva_area = Area(codigo_area=codigo, nombre_area=nombre, cantidad_funcionarios=cantidad)

                    if not self.organigrama.get_root():
                        self.organigrama.create_area(area=nueva_area, parent=None)
                        print("Agregado area como raiz del organigrama")
                        continue

                    if self.organigrama.get_root():
                        codigo_area = int(input(self.cursor.format("Codigo del area padre a asignar")) or 0)
                        area = self.organigrama.get_root().find(codigo_area)
                        if area:
                            area.agregar_area_hija(nueva_area)
                        print("Agregado al area {}".format(codigo_area))
                    # else:
                    #     # organigrama._raiz = nueva_area
                    #     organigrama.create_area(area=nueva_area, parent=None)
                    #     print("Agregado area como raiz del organigrama")

                elif comando == 'b':
                    # quitar nodo
                    codigo = int(input(self.cursor.format("Codigo del area a borrar")))
                    if self.organigrama.get_root():
                        self.organigrama.get_root().borrar_area(codigo)
                    else:
                        print("Organigrama sin areas definidas")

                # elif comando == 'i':
                #     # imprimir organigrama
                #     if organigrama.raiz:
                #         organigrama.raiz.imprimir_jerarquia()
                #     else:
                #         print "Organigrama sin areas definidas"

                # elif comando == 's':
                #     # sumorg
                #     codigo_padre = int(input(cursor.format("ingrese codigo de area a ejecutar sumorg(?)")))
                #     if codigo_padre:
                #         valor = organigrama.raiz.sumorg(codigo_padre)
                #         print "sumorg({}) = {}".format(codigo_padre, valor)

                elif comando == 'x':
                    # terminar loop
                    self.running = False
                    print("** Fin **")

            else:
                print("Comando invalido")


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
