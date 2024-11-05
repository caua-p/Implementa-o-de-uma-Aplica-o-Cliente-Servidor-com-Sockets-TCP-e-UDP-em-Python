import socket
import threading

def tratar_cliente_tcp(conexao, endereco_cliente):
    print(f"Conexão TCP estabelecida com {endereco_cliente}")
    mensagem = conexao.recv(1024).decode('utf-8')
    print(f"Recebido de {endereco_cliente} via TCP: {mensagem}")
    resposta = f"TCP: {mensagem}"
    conexao.send(resposta.encode('utf-8'))
    conexao.close()
    print(f"Conexão TCP com {endereco_cliente} encerrada")

def tratar_requisicoes_udp(servidor_udp):
    while True:
        mensagem, endereco_cliente = servidor_udp.recvfrom(1024)
        print(f"Recebido de {endereco_cliente} via UDP: {mensagem.decode('utf-8')}")
        resposta = f"UDP: {mensagem.decode('utf-8')}"
        servidor_udp.sendto(resposta.encode('utf-8'), endereco_cliente)

def main():
    servidor_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_tcp.bind(('0.0.0.0', 5000))
    servidor_tcp.listen(5)
    print("Servidor TCP ouvindo na porta 5000")

    servidor_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servidor_udp.bind(('0.0.0.0', 5001))
    print("Servidor UDP ouvindo na porta 5001")

    thread_udp = threading.Thread(target=tratar_requisicoes_udp, args=(servidor_udp,))
    thread_udp.start()

    while True:
        conexao, endereco_cliente = servidor_tcp.accept()
        thread_tcp = threading.Thread(target=tratar_cliente_tcp, args=(conexao, endereco_cliente))
        thread_tcp.start()

if __name__ == "__main__":
    main()
