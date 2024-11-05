import socket
import threading

def tratar_cliente(conexao, endereco_cliente):
    print(f"Conexão estabelecida com {endereco_cliente}")
    mensagem = conexao.recv(1024).decode('utf-8')
    print(f"Recebido de {endereco_cliente}: {mensagem}")
    resposta = f"TCP: {mensagem}"
    conexao.send(resposta.encode('utf-8'))
    conexao.close()
    print(f"Conexão com {endereco_cliente} encerrada")

def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind(('0.0.0.0', 5000))
    servidor.listen(5)
    print("Servidor TCP ouvindo na porta 5000")

    while True:
        conexao, endereco_cliente = servidor.accept()
        thread_cliente = threading.Thread(target=tratar_cliente, args=(conexao, endereco_cliente))
        thread_cliente.start()

if __name__ == "__main__":
    main()
