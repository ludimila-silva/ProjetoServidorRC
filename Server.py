import socket

pe = open('src/pedra3.png', 'rb')
pa = open('src/papel2.png', 'rb')
te = open('src/tesoura1.png', 'rb')
pedra = pe.read()
papel = pa.read()
tesoura = te.read()
# h = open('index.html', 'r') #abri o arquivo idenx.html no modo reading
h = open('Projeto LPF - joquempo.html', 'r')
homepage = h.read()  # a variavel homepage recebe a leitura do index.html

# acessa o pacote socket impportado do pacote python e o .socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# cria um novo objeto do socket

# O socket.AF_INET é o protocolo de internet e o socket.SOCK_STREAM é protocolo de TCP

print(s)  # apresenta pro usuario o objeto criado no socket

s.bind(('', 5150))  # cria o acesso ao servidor usando a porta 1318
s.listen(5)  # listen é a quantidade e clientes que o servidor 'escuta', que os ervidor aceita, apos esses 5 ele bloqueia

try:
    while True:  # ficará tentando ate que aja um break do usuario ou sistema
        ws, addr = s.accept()
        # Aguarda uma conexão de entrada. Então retorna um novo soquete representando a conexão e o
        # endereço do cliente. Para soquetes ip, a informação de endereço é um par
        # WS recebe a parte do websocket e o addr recebe a segunda parte chamada no s.accept
        data = ws.recv(2048)
        # ws.recv aguarda o recebimento de no maximo 2000 Bytes
        P = data.split(b' ')  # GET / HTTP/1.1 -> [GET, /, HTTP/1.1]
        # o data.split transforma essa string em uma lista
        if P[0] == b'GET':  # caso o primeiro item for 'GET' ele segue a logica
            # e se o segundo item for '/' ele continua a logica
            if P[1] == b'/':
                # resp = response segue o fluxo server -> client, onde client é um browser
                # abaixo descrito o formato da mensagem response da forma que o navegador lerá
                resp = ('HTTP/1.1 200 OK\r\n' + 'Content-Type: text/html\r\n' + 'Content-Length: ' +
                        str(len(homepage)) + '\r\n\r\n' + (homepage))
                # "HTTP/1.1 200 OK\r\n" = confirma a conexao com o protocolo solicitado
                # "Content-Type: text/html\r\n" = informa o tipo de conteudo que sera mostrado, no nosso caso um texto html
                # "Content-Length: ' + str(len(homepage))" = informa o tamanho do texto utilizado, para isso ele le o tamanho da string que é composta do texto html
                # "\r\n\r\n" = quebra dupla de linha para informar ao navegador que após isso é informado os dados da página
                # "homepage" = chama a variavel que armazena a leitura do texto html requerido anteriormente
                resp = str.encode(resp)
                # str.enconde = codifica de string para Byte a meNsagem response para poder ser enviada ao navegador na forma que ele possa le-la, tranformando em um codigo de versao UTF-8
                # no navegador ele utiliza a função decode que reconhece a linguagem utf-8, esse modo também pode ser utilizado por um outro client criado
                ws.sendall(resp)# envia a mensagem para o websocket, ou seja o client(que no nosso caso é o navegador)

except KeyboardInterrupt:  # se o server utilizar comando ctrl+c encerrará a conexão
    print(" terminado pelo usuario")
    ws.close()  # fecha o websocket
    s.close()  # fecha o pacote socket importado
