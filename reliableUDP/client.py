import socket as s
import time

# Definir um número de sequência inicial
sequence_number = 0

def checksum(data, sequence_number):
    data = sequence_number.to_bytes(4, byteorder="big") + data

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

    return checksum_value

def ping(host, port):
    global sequence_number
    client = s.socket(s.AF_INET, s.SOCK_DGRAM)
    addr = (host, port)

    while True:
        message = input("Digite uma mensagem (ou 'quit' para encerrar): ")
        
        if message.lower() == 'quit':
            print("Encerrando a aplicação.")
            client.close()  # Fecha o socket do cliente
            break
        
        message_bytes = message.encode("utf-8")
        sequence_number += 1
        sequence_bytes = sequence_number.to_bytes(4, byteorder="big")

        data = sequence_bytes + message_bytes

        # Define um temporizador (timeout) para aguardar a resposta
        client.settimeout(1)
        start_time = time.time()

        # Enviar dados com número de sequência e mensagem
        checksum_value = checksum(data, sequence_number)
        checksum_bytes = checksum_value.to_bytes(2, byteorder="big")
        client.sendto(checksum_bytes, addr)
        client.sendto(data, addr)

        try:
            # Aguardar resposta e receber o número de sequência do servidor
            data, addr = client.recvfrom(1024)
            server_sequence_number = int.from_bytes(data[0:4], byteorder="big")
            if server_sequence_number == sequence_number:
                print(f"Resposta do servidor: {data[4:].decode('utf-8')}")
            else:
                print("Número de sequência incorreto na resposta do servidor.")
        except s.timeout:
            print("Tempo limite atingido, reenviando...")
            if time.time() - start_time > 5:
                print("Tempo limite máximo atingido, desistindo.")
                break  # Desista após um limite máximo de tempo

if __name__ == "__main__":
    HOST = s.gethostbyname(s.gethostname())
    PORT = 8080

    ping(HOST, PORT)
