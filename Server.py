import socket
import threading

clave = {
    "Juan": "1234",
    "Ana": "4321",
    "Cris": "2341"
}
Usuario_conectados=[]


hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
print("Tu computadora es " + hostname)
print("IP de la computadora: " + ip)


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((ip, 12345))
server_socket.listen(3)

def manejar_usuarios(cliente_socket):
    try:
        usuario = cliente_socket.recv(1024).decode()
        print("Usuario recibido:", usuario)
        
        contraseña = cliente_socket.recv(1024).decode()
        print("Contraseña recibida:", contraseña)

        if usuario in clave and clave[usuario] == contraseña:
            cliente_socket.send("Login correcto".encode())
            cliente_socket.send("Escriba cual de esta 2 opciones utilizar: /old mensaje o /user mensaje".encode())
            for i in range(1):
                valor=usuario
                Usuario_conectados.append(valor)
                print(Usuario_conectados)
            
            opcion = cliente_socket.recv(1024).decode()
            print("Opción recibida de {usuario}: {opcion}")

            if opcion.startswith("/old"):
                cliente_socket.send("eligio /old".encode())
                mensaje_opciones=cliente_socket.recv(1024).decode()
               
            elif opcion.startswith("/user"):
                cliente_socket.send("eligio /user".encode())
            else:
                cliente_socket.send("la opcion no existe".encode())
        else:
            cliente_socket.send("no exite la cuenta".encode())
    except Exception as e:
        print("Error:", e)
    finally:
        cliente_socket.close()

while True:
    cliente_socket, address = server_socket.accept()
    print("Conexión desde:", address)
    threading.Thread(target=manejar_usuarios, args=(cliente_socket,)).start()
