import socket as s
import random

# Inicializa o número de sequência do servidor
server_sequence_number = 0

# Função para verificar o checksum
def verify_checksum(data, checksum):
    byte_count = len(data)
    print(f"N. bytes: {byte_count}")
    if byte_count % 2 == 1:
        data += b'\x00'
        byte_count += 1

    checksum_value = 0

    for i in range(0, byte_count, 2):
        w = (data[i] << 8) + data[i + 1]
        checksum_value += w
        checksum_value = (checksum_value >> 16) + (checksum_value & 0xFFFF)

    checksum_value = ~checksum_value & 0xFFFF

    return checksum_value == checksum

if __name__ == "__main__":
    HOST = s.gethostbyname(s.gethostname())
    PORT = 8080
    server = s.socket(s.AF_INET, s.SOCK_DGRAM)
    server.bind((HOST, PORT))

    while True:
        checksum_bytes, addr = server.recvfrom(1024)
        checksum = int.from_bytes(checksum_bytes, byteorder="big")
        data, addr = server.recvfrom(1024)

        # Obtém o número de sequência dos primeiros 4 bytes dos dados
        client_sequence_number = int.from_bytes(data[0:4], byteorder="big")

        data = data[4:]  # Remove os primeiros 4 bytes que representam o número de sequência

        print(f"Cliente: {data.decode('utf-8')}")

        # Simula um erro de integridade aleatório
        integrity_error = random.randint(0, 100)
        if integrity_error <= 25 or client_sequence_number != server_sequence_number:
            print("Pacote contém erro de integridade ou número de sequência incorreto.")
            server.sendto(b"ERRO", addr)
        else:
            if verify_checksum(data, checksum):
                print("Checksum é válido.")
            else:
                print("Checksum é inválido.")

            # Atualiza o número de sequência do servidor
            server_sequence_number += 1

            # Envia o número de sequência de volta ao cliente como confirmação
            server.sendto(client_sequence_number.to_bytes(4, byteorder="big") + b"ACK", addr)
