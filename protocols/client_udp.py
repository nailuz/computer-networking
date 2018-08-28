import socket
HOST = '127.0.0.1'  # Endereco IP do Servidor
PORT = 5100            # Porta que o Servidor esta
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)
print 'Para sair use CTRL+X\n'
msg = raw_input()
while msg <> '\x18':
    udp.sendto (msg, dest)
    print (udp.recvfrom(1024))
    msg = raw_input()
print 'Para sair use CTRL+X\n'
msg = input()
while msg != '\x18':
    udp.sendto (msg.escode(), dest)
    print (udp.recvfrom(1024))
    msg = input()
udp.close()