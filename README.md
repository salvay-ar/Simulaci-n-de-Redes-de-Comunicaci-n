# Simulación de Red en Python
## Descripción

Este proyecto simula una red de comunicación usando Programación Orientada a Objetos en Python. Se implementa un servidor y tres clientes que intercambian mensajes.


## Estructura

Se utiliza la clase Nodo con los siguientes métodos:

__ init __: inicializa el nodo

agregar_conexion: conecta nodos

enviar_mensaje: envía mensajes

recibir_mensaje: recibe mensajes


## Funcionamiento
 
Se crea 1 servidor y 3 clientes.
El servidor se conecta con los clientes.
El servidor envía un mensaje a todos los nodos conectados.


## Ejecución
python simulacion_de_redes.py




# Simulación de Red con conexión y desconexión dinámica
## Descripción

Simulación de una red en Python con 1 servidor y 3 clientes, incluyendo desconexión y reconexión dinámica.

## Funcionalidad

Clase Nodo con:

agregar_conexion

eliminar_conexion

enviar_mensaje

recibir_mensaje

reconexion (usa time.sleep(2))

## Comportamiento
El servidor envía un mensaje.
Antes de enviarlo:

Se desconecta un cliente.

Se muestra: “Simulando desconexión y reconexión dinámica…”

Se espera 2 segundos.

Se reconecta el cliente.

Luego todos reciben el mensaje.

##Ejecutar

python simulacion_de_red_con_desconexcion_dinamica.py
