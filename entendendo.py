import socket

h = open('index.html', 'r')
homepage = h.read()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

s.bind(('', 1318))
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

        P = data.split(' ')
        print('P\n')
        print(P)
        print('\n\n')

        if P[0] == 'GET':
            if P[1] == '/':
                resp = ('HTTP/1.1 200 OK\r\n' + 'Content-Type: text/html\r\n' +
                        'Content-Length: ' + str(len(homepage)) + '\r\n\r\n' + (homepage))
                print('resp\n')
                print(resp)
                print('\n\n')
                resp = str.encode(resp)
                print('resp encode\n')
                print(resp)
                print('\n\n')
                ws.sendall(resp)

except KeyboardInterrupt:
    print("terminado pelo usuario")
    ws.close()
    s.close()