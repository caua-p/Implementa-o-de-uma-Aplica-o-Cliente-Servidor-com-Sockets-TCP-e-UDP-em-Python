import socket

def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servidor.bind(('0.0.0.0', 5001))
    print("Servidor UDP ouvindo na porta 5001")

    while True:
        mensagem, endereco_cliente = servidor.recvfrom(1024)
        print(f"Recebido de {endereco_cliente}: {mensagem.decode('utf-8')}")
        resposta = f"UDP: {mensagem.decode('utf-8')}"
        servidor.sendto(resposta.encode('utf-8'), endereco_cliente)

if __name__ == "__main__":
    main()
