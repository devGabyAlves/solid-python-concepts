# D - Principio da Inversao da Dependencia (DIP)
""""
Modulos de alto nivel nao devem depender diretamente dos modeulos de baixo nivel

Os sistemas mais flexiveis sao aqueles em que as dependencias do codigo-fonte referem-se apenas a abstracoes, nao a concrecoes
"""

from .notificator_interface import NotificatorInterface


class ClientService:
    def __init__(self, notificator: NotificatorInterface) -> None:
        self.notificator = notificator

    def send(self, message: str) -> None:
        self.notificator.send_notification(message)