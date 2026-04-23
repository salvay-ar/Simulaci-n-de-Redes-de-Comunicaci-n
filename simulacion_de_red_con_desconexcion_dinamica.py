import time
import os
os.system("cls")
class Nodo:

    def __init__(self, tipo):
        self.tipo = tipo
        self.conexiones = [] 

    def agregar_conexion(self, nodo):
        self.conexiones.append(nodo) # Se guarda en el servidor una lista con los clientes

    def eliminar_conexion(self, nodo):
        self.conexiones.remove(nodo)
        
    def enviar_mensaje(self, mensaje, nodo):
        self.reconexion(nodo) # Cuando se envia un mensaje, se simula una desconexion y reconexión con los nodos que recibirán el mensaje
        print(f"{self.tipo} está enviando el mensaje: '{mensaje}'")  # Recibe el tipo y el mensaje

        for conexion in self.conexiones:  # Busca cada conexion guardada en las conexiones de la clase que envio el mensaje
             conexion.recibir_mensaje(mensaje, self.tipo)  # Cada una de las clases conectadas llama al otro método 
                                                           #(recibir_mensaje), envía el mensaje y quién lo envió
    
    def reconexion(self, nodo):
        self.eliminar_conexion(nodo) # Desconectamos el nodo
        print("Simulando desconexión y reconexión dinámica...")
        print(f"Reconectando...")
        time.sleep(2) #Esperamos 2 segundos
        
        self.agregar_conexion(nodo) # Volvemos a añadir al nodo a la lista de conexiones
        os.system("cls")
        print("¡Hola de nuevo a todos!")        
        
    
    def recibir_mensaje(self, mensaje, remitente): 
        print(f"{self.tipo} recibió el mensaje de {remitente}: '{mensaje}'") 


#Se crea cada clase
servidor = Nodo("Servidor")
cliente1 = Nodo("Cliente1")
cliente2 = Nodo("Cliente2")
cliente3 = Nodo("Cliente3")

#Conecta el servidor a todos los clientes
servidor.agregar_conexion(cliente1)
servidor.agregar_conexion(cliente2)
servidor.agregar_conexion(cliente3)

#Conectar los clientes al servidor (Para que también puedan enviar mensajes)
cliente1.agregar_conexion(servidor)
cliente2.agregar_conexion(servidor)
cliente3.agregar_conexion(servidor)


servidor.enviar_mensaje("Hola clientes", cliente1)
        
                    