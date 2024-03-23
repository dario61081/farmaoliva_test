__version__ = "1.0"
__author__ = "Dario Garcia"

from entidades import Organigrama
from funciones.actions import ActionOrganigramaAddArea, ActionOrganigramaRender, IOrganigramaAction, \
    ActionOrganigramaRemoveArea, ActionOrganigramaTotalizar, ActionOrganigramaExport, ActionOrganigramaImport


class ControllerOrganigrama:
    """
    Controlador de organigrama
    """

    def __init__(self, *, organigrama: Organigrama) -> None:
        """
        Constructor de controlador
        :param organigrama:
        """
        self.organigrama: Organigrama = organigrama
        self.running: bool = True
        self.cursor: str = "{} > "
        self.actions: dict = {}
        self.actions_titles: dict = {}

        # registrar acciones
        self.register_action(key="a", title="Nuevo", action=ActionOrganigramaAddArea)
        self.register_action(key="b", title="Borrar", action=ActionOrganigramaRemoveArea)
        self.register_action(key="i", title="Imprimir", action=ActionOrganigramaRender)
        self.register_action(key="t", title="Totalizar", action=ActionOrganigramaTotalizar)
        self.register_action(key="e", title="exportar", action=ActionOrganigramaExport)
        self.register_action(key="l", title="Importar", action=ActionOrganigramaImport)

    def register_action(self, *, key: str, title: str, action: IOrganigramaAction) -> None:
        """
        Registrar una acción
        :param key: tecla de acceso
        :param title: titulo
        :param action: action a ejecutar
        :return: None
        """
        self.actions[key] = action
        self.actions_titles[key] = title.capitalize()

    def print_actions(self) -> str:
        """
        Imprimir menu de acciones
        :return: str
        """
        return "|".join([" {}:{} ".format(k, v) for k, v in self.actions_titles.items()])

    def execute_action(self, key: str, organigrama: Organigrama, **kwargs) -> None:
        """
        Ejecutar acción
        :param key: tecla de acceso
        :param organigrama: Organigrama en la que se ejecuta la acción
        :param kwargs: parametros varios
        :return: None
        """
        try:
            self.actions[key]()(organigrama, **kwargs)
        except KeyError:
            print("(!) Acción no encontrada")

    def execute(self) -> None:
        """
        Ejecutar controlador
        :return: None
        """

        self.execute_action('i', self.organigrama)
        menu: str = f"Acciones: {self.print_actions()}| x:Salir $ "

        while self.running:

            comando = input(self.cursor.format(menu))
            if comando == "x":
                print("Saliendo...")
                self.running = False
                break

            self.execute_action(comando, self.organigrama)
