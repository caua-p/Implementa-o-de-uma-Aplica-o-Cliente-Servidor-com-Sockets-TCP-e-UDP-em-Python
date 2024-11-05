import socket

def main():
    protocolo = input("Escolha o protocolo (TCP/UDP): ").strip().upper()
    mensagem = input("Digite a mensagem a ser enviada: ")

    if protocolo == 'TCP':
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect(('127.0.0.1', 5000))
        cliente.send(mensagem.encode('utf-8'))
        resposta = cliente.recv(1024).decode('utf-8')
        print(f"Resposta do servidor: {resposta}")
        cliente.close()
    elif protocolo == 'UDP':
        cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        cliente.sendto(mensagem.encode('utf-8'), ('127.0.0.1', 5001))
        resposta, _ = cliente.recvfrom(1024)
        print(f"Resposta do servidor: {resposta.decode('utf-8')}")
    else:
        print("Protocolo inválido. Escolha entre TCP e UDP.")

if __name__ == "__main__":
    main()
