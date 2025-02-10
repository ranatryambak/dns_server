import socket

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg = b'\xaa\xbb' + b'\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00' + b'\x06google\x03com\x00\x00\x01\x00\x01'
address = ('8.8.8.8',53)

sock.sendto(msg,address)

data,addr = sock.recvfrom(512)

print(f"the data recieved from {addr} is {data.hex()}")

sock.close()