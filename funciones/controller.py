__version__ = "1.0"
__author__ = "Dario Garcia"

from entidades import Organigrama
from funciones.actions import ActionOrganigramaAddArea, ActionOrganigramaRender, IOrganigramaAction, \
    ActionOrganigramaRemoveArea, ActionOrganigramaTotalizar


class ControllerOrganigrama:
    """
    Controlador de organigrama
    """

    def __init__(self, *, organigrama: Organigrama) -> None:
        self.organigrama = organigrama
        self.running = True
        self.cursor = "{} > "
        self.actions = {}

        # registrar acciones
        self.register_action("a", ActionOrganigramaAddArea)
        self.register_action("b", ActionOrganigramaRemoveArea)
        self.register_action("i", ActionOrganigramaRender)
        self.register_action("t", ActionOrganigramaTotalizar)

    def register_action(self, name: str, action: IOrganigramaAction) -> None:
        self.actions[name] = action

    def execute_action(self, name: str, organigrama: Organigrama, **kwargs) -> None:
        try:
            self.actions[name]()(organigrama, **kwargs)
        except KeyError:
            print("(!) Acción no encontrada")

    def execute(self) -> None:

        self.execute_action('i', self.organigrama)

        while self.running:

            comando = input(
                self.cursor.format("Accion: (a: nuevo | b: borrar | i: imprimir | t: totalizar | x: salir "))
            if comando == "x":
                print("Saliendo...")
                self.running = False
                break

            self.execute_action(comando, self.organigrama)
