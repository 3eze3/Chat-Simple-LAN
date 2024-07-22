# Chat Simple en Red LAN

Este proyecto implementa un chat simple utilizando sockets para la comunicación entre múltiples dispositivos en una red LAN. A través de este chat, los clientes pueden intercambiar mensajes en tiempo real, y el servidor se encarga de distribuir los mensajes a todos los clientes conectados, excepto al remitente.

## Funcionalidades

- **Servidor**: Gestiona las conexiones de los clientes y distribuye los mensajes a todos los clientes conectados.
- **Cliente**: Permite a los usuarios enviar y recibir mensajes en tiempo real.

## Video del Funcionamiento

Para ver el chat en acción, consulta el siguiente video:
[Ver video del chat en funcionamiento](URL_DEL_VIDEO)

## Uso del Script

### Clonar el Repositorio

Primero, clona el repositorio a tu máquina local:

```bash
$ git clone https://github.com/3eze3/Chat-Simple-LAN.git

```

### Configuración del Servidor

Para iniciar el servidor, navega a la carpeta del repositorio y ejecuta el siguiente comando:

```bash

$ python3 server.py IPv4 Port

```

Reemplaza `IPv4` con la dirección IP del servidor y `Port` con el puerto que deseas usar.

### Configuración del Cliente

Para conectar un cliente al servidor, ejecuta el siguiente comando en otra máquina en la misma red:

```bash

$ python3 client.py IPv4 Port

```

De nuevo, reemplaza `IPv4` con la dirección IP del servidor y `Port` con el puerto utilizado por el servidor.

### Ejemplos

**Servidor**:

```bash
$ python3 server.py 192.168.1.10 5000

```

**Cliente**:

```bash
$ python3 client.py 192.168.1.10 5000

```
