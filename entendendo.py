import socket
import string

h = open('projeto LPF - joquempo.html', 'r')
homepage = h.read()
pe = open('src/pedra3.png', 'rb')
pedra = pe.read()
pa = open('src/papel2.png', 'rb')
papel = pa.read()
te = open('src/tesoura1.png', 'rb')
tesoura = te.read()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

s.bind(('', 5150))
s.listen(5)

try:
    while True:
        ws, addr = s.accept()
        print('ws\n')
        print(ws)
        print('\n\n')

        data = ws.recv(2000)
        print('data\n')
        print(data)
        print('\n\n')

        P = data.split(b' ')
        print('P\n')
        print(P)
        print('\n\n')

        if P[0] == b'GET':
            if P[1] == b'/':
                if P[2] == b'HTTP/1.1\r\nHost:':
                    resp = ('HTTP/1.1 200 OK\r\n' + 'Content-Type: text/html\r\n' +
                            'Content-Length: ' + str(len(homepage)) + '\r\n\r\n' + (homepage))
                    print('resp\n')
                    print(resp)
                    print('\n\n')
                    resp = str.encode(resp)
                    resp = resp
                    print('resp encode\n')
                    print(resp)
                    print('\n\n')
                    ws.sendall(resp)

            if P[1] == b'/favicon.ico':
                resp = ('HTTP/1.1 200 OK\r\n' + 'Content-Type: image/png\r\n' +
                        'Content-Length: ' + str(len(tesoura)) + '\r\n\r\n')
                print('resp\n')
                print(resp)
                print('\n\n')
                resp = str.encode(resp)
                resp = resp+tesoura
                ws.sendall(resp)
            if P[1] == b'/src/pedra3.png':
                resp = ('HTTP/1.1 200 OK\r\n' + 'Content-Type: image/png\r\n' +
                        'Content-Length: ' + str(len(pedra)) + '\r\n\r\n')
                print('resp\n')
                print(resp)
                print('\n\n')
                resp = str.encode(resp)
                resp = resp+pedra
                ws.sendall(resp)
            if P[1] == b'/src/papel2.png':
                resp = ('HTTP/1.1 200 OK\r\n' + 'Content-Type: image/png\r\n' +
                        'Content-Length: ' + str(len(papel)) + '\r\n\r\n')
                print('resp\n')
                print(resp)
                print('\n\n')
                resp = str.encode(resp)
                resp = resp+papel
                ws.sendall(resp)
            if P[1] == b'/src/tesoura1.png':
                resp = ('HTTP/1.1 200 OK\r\n' + 'Content-Type: image/png\r\n' +
                        'Content-Length: ' + str(len(tesoura)) + '\r\n\r\n')
                print('resp\n')
                print(resp)
                print('\n\n')
                resp = str.encode(resp)
                resp = resp+tesoura
                ws.sendall(resp)


except KeyboardInterrupt:
    print("terminado pelo usuario")
    ws.close()
    s.close()
