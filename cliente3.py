import socket

mi_socket = socket.socket()
mi_socket.connect(('10.120.3.188', 12345)) 

print("Ahora ingres el usuari y contraseña")
usuario = input("Usuario: ")
contraseña = input("Contraseña: ")
mi_socket.send(usuario.encode())
mi_socket.send(contraseña.encode())



respuesta = mi_socket.recv(1024).decode()
print(respuesta)

if "Login correcto" in respuesta:
   
    mensaje_opciones = mi_socket.recv(1024).decode()
    print(mensaje_opciones)

   
    opcion = input("Ingrese opción: ")
    mi_socket.send(opcion.encode())

    
    respuesta_opcion = mi_socket.recv(1024).decode()
    print(respuesta_opcion)
else:
    print("el u2suario no existe")

mi_socket.close()
