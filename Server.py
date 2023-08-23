import socket  # Importa o socket
# import _thread
HOST = "172.16.226.235"  # Endereço IP do host
PORT = 65433  # Porta a ser escutada
# # Função para o recebimento dos valores que os clientes mandam
# def receive_values(data, addr):
#     while True:
#         text = bytearray(len(data))
#         for i in range(len(data)):
#             text[i] = data[i]
#         f = open("./textFiles/" + str(addr) + ".txt", "a")
#         f.write(text.decode("utf-8"))
#         f.close()

# Definindo um limite para o socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    while True:
        addressPair = s.recvfrom(1024)
        print(f"Conexao estabelecida com {addressPair[1]}")
        data = addressPair[0]
        addr = addressPair[1]
        text = bytearray(len(data))
        for i in range(len(data)):
            text[i] = data[i]
        f = open("./textFiles/" + str(addr) + ".txt", "a")
        f.write(text.decode("utf-8"))
        f.close()
