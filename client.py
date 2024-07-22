import socket
import pickle
import threading
import sys


def recive_message(cliente_socket):
    try:
        while True:
            data = cliente_socket.recv(1024)
            if not data:
                break
            nombre, message = pickle.loads(data)
            print(f"\n[*] {nombre}: {message}\n")
            print("\n[+] Enviar mensaje al servidor")
    except Exception as e:
        print(f"\n[!] Error recibiendo mensaje: {e}")
    finally:
        cliente_socket.close()


def start_chat_client(ip, puerto):

    server = (ip, puerto)
    cl_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cl_socket.connect(server)
    nombre_usuario = input("\n[+] Ingrese su nombre: ")

    recive_thread = threading.Thread(target=recive_message, args=(cl_socket,))
    recive_thread.start()

    try:
        while True:
            menssage = input(f"\n[+] {nombre_usuario.title()}"
                             f" enviar mensaje al servidor: {server[0]}: ")
            if menssage.strip().lower() == "bye":
                break
            data_to_send = pickle.dumps((nombre_usuario, menssage))
            cl_socket.sendall(data_to_send)
    except BrokenPipeError:
        print("[!] Conexión cerrada por el servidor.")
    finally:
        cl_socket.close()


if len(sys.argv) < 3:
    print(f"[!] Uso de script: {sys.argv[0]} IPv4 Port")
else:
    ip = sys.argv[1]
    puerto = int(sys.argv[2])
    start_chat_client(ip, puerto)
