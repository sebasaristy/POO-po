from abc import ABC, abstractmethod

class MedioComuniacion(ABC):

    @abstractmethod
    def enviar_mensaje(self, mensaje):
        ...
    
class CorreoElectronico(MedioComuniacion):

    def enviar_mensaje(self, mensaje):
        print("Mensaje enviado por correo electronico: ",mensaje)

class SMS(MedioComuniacion):

    def enviar_mensaje(self, mensaje):
        print("Mensaje enviado por SMS: ",mensaje)

class Push(MedioComuniacion):

    def enviar_mensaje(self, mensaje):
        print("Mensaje enviado por notificacion al celular: ",mensaje)

class Whatsapp(MedioComuniacion):

    def enviar_mensaje(self, mensaje):
        print("Mensaje enviado por wasap: ",mensaje)

class FactoryMedios:

    @staticmethod
    def crear_medio(tipo):
        if tipo == "correo":
            return CorreoElectronico()
        elif tipo == "sms":
            return SMS()
        elif tipo == "push":
            return Push()
        elif tipo == "whatsapp":
            return Whatsapp()
        else:
            raise ValueError("Medio de comunacion no existe")
    
class GestorEnvios:
    def __init__(self, tipos):
        self.tipos = [FactoryMedios.crear_medio(t) for t in tipos]
    
    def enviar_mensaje(self, mensaje):
        for t in self.tipos:
            t.enviar_mensaje(mensaje)

gestor = GestorEnvios(["correo", "whatsapp"])
gestor.enviar_mensaje("Hola")