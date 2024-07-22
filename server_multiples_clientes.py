import socket
import pickle
import threading
import sys


clientes_conectados = []
clientes_lock = threading.Lock()


class ClienteThread(threading.Thread):

    def __init__(self, cliente_socket, cliente_addr):
        super().__init__()
        self.cliente_socket = cliente_socket
        self.cliente_addr = cliente_addr

        print(f"\n[*] Nuevo cliente conectado: {cliente_addr}")

        with clientes_lock:
            clientes_conectados.append(cliente_socket)

    def message_broadcast(self, message, nombre):
        for cliente in clientes_conectados:
            if cliente != self.cliente_socket:
                try:
                    message = (nombre, message)
                    data_send_all_clientes = pickle.dumps(message)
                    cliente.sendall(data_send_all_clientes)
                except Exception as e:
                    print(f"[!] Error al enviar mensaje a"
                          f"{cliente.getpeername()}: {e}")
                    cliente.close()
                    if cliente in clientes_conectados:
                        clientes_conectados.remove(cliente)

    def run(self):
        try:
            while True:
                data = self.cliente_socket.recv(1024)
                if not data:
                    break

                nombre, message = pickle.loads(data)

                if message.strip().lower() == "bye":
                    break

                with clientes_lock:
                    if len(clientes_conectados) == 0:
                        print("\n[*] Servidor desconectado...")
                        break
                    self.message_broadcast(message, nombre)
        except Exception as e:
            print(f"[!] Error en el hilo {self.cliente_socket}: {e}")
        finally:
            with clientes_lock:
                if self.cliente_socket in clientes_conectados:
                    clientes_conectados.remove(self.cliente_socket)
            self.cliente_socket.close()
            print(f"\n [*] Cliente {self.cliente_addr} desconectado")


def start_server(ip, port):
    server = (ip, port)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind(server)
        server_socket.listen()
        print("\n[*] En espera de conexiones...\n")

        while True:
            cliente_socket, cliente_addr = server_socket.accept()
            new_thread_client = ClienteThread(cliente_socket, cliente_addr)
            new_thread_client.start()


if len(sys.argv) < 3:
    print(f"[!] Uso del scritp: {sys.argv[0]} Ipv4 Puerto")
    sys.exit(1)
else:
    ip = sys.argv[1]
    puerto = int(sys.argv[2])
    start_server(ip, puerto)
