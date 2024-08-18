import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 1313)
sock.bind(server_address)

sock.listen(1)

print('Waiting for a client to connect')
client, client_port = sock.accept()
print('Connection from client %s:%s' % client_port)

request = client.recv(14)
print('Client sent "%s"' % request.decode())
reply = b'And Beyond!'
print('Server replies "%s"' % reply.decode())
client.sendall(reply)

client.close()
input("prompt: ")