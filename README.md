# Implementa-o-de-uma-Aplica-o-Cliente-Servidor-com-Sockets-TCP-e-UDP-em-Python
# Aplicação Cliente/Servidor com Sockets TCP e UDP em Python

## Descrição do Projeto
Este projeto consiste na implementação de uma aplicação cliente/servidor em Python, utilizando os protocolos de transporte TCP e UDP. O objetivo é demonstrar as diferenças na implementação e no uso desses protocolos, bem como praticar a programação de redes e o uso de threads para atender múltiplas conexões simultaneamente.

## Estrutura do Projeto
O projeto é composto pelos seguintes arquivos:

- `servidor_tcp.py`: Código do servidor que utiliza o protocolo TCP.
- `servidor_udp.py`: Código do servidor que utiliza o protocolo UDP.
- `cliente.py`: Código do cliente que se comunica com os servidores, escolhendo entre TCP e UDP.
- `servidor.py`: Implementação combinada dos servidores TCP e UDP com suporte a threads.
- `README.md`: Documentação do projeto com instruções detalhadas.

## Funcionalidades
### Servidor TCP
- Escuta conexões na porta 5000.
- Atende múltiplos clientes simultaneamente usando threads.
- Responde com uma mensagem prefixada com "TCP:".

### Servidor UDP
- Escuta conexões na porta 5001.
- Recebe mensagens de clientes e responde com uma mensagem prefixada com "UDP:".

### Cliente
- Permite ao usuário escolher entre os protocolos TCP e UDP.
- Envia uma mensagem ao servidor e exibe a resposta na tela.
