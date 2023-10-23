Relatório do Código do Cliente e Servidor

Aplicação Cliente-Servidor com Verificação de Integridade

1. Código do Cliente:

O código do cliente é responsável por enviar mensagens para o servidor com verificação de integridade usando um número de sequência e um checksum. Ele também lida com respostas do servidor e possui um temporizador para reenviar mensagens se a resposta do servidor não for recebida a tempo.

Principais Características:

Gera um número de sequência para cada mensagem enviada.
Calcula um checksum para as mensagens e inclui o número de sequência.
Possui um temporizador para aguardar a resposta do servidor.
Lida com respostas do servidor, verificando o número de sequência.
Encerra a aplicação com a entrada "quit".
2. Código do Servidor:

O código do servidor é responsável por receber mensagens do cliente, verificar a integridade dos dados e enviar reconhecimentos (ACK) se a mensagem for válida. Ele também simula erros de integridade para fins de demonstração.

Principais Características:

Recebe mensagens do cliente com um número de sequência e checksum.
Verifica a integridade dos dados usando o checksum.
Simula erros de integridade aleatórios (25% de probabilidade).
Envia "ERRO" se a mensagem estiver corrompida e um ACK se for válida.
Manual de Utilização:

Aplicação Cliente-Servidor com Verificação de Integridade

Cliente:

Inicialização:

Execute o código do cliente em um ambiente Python compatível.
Envio de Mensagens:

O cliente solicitará que você digite uma mensagem.
Digite sua mensagem e pressione "Enter".
Para encerrar a aplicação, digite "quit" e pressione "Enter".
Recebimento de Respostas:

Após o envio de uma mensagem, o cliente aguardará uma resposta do servidor.
O cliente verificará o número de sequência da resposta para garantir a ordem correta.
A resposta do servidor será exibida no console.
Servidor:

Inicialização:

Execute o código do servidor em um ambiente Python compatível.
Esperando Mensagens:

O servidor está configurado para ouvir mensagens do cliente em um endereço e porta específicos.
Ele aguardará as mensagens do cliente.
Simulação de Erros (Opcional):

Se você não deseja simular erros de integridade, siga as instruções na seção "Se Eu Não Quiser Simular a Falha de Integridade" no código do servidor (como explicado anteriormente) para remover a simulação.
Respostas do Servidor:

O servidor responderá com um reconhecimento (ACK) se receber uma mensagem válida do cliente.
Em caso de simulação de erro, o servidor responderá com "ERRO".
Observações:

O código do servidor foi projetado para demonstrar a verificação de integridade de mensagens e a simulação de erros de integridade.
A aplicação é uma simplificação para fins de aprendizado e demonstração. Em aplicações reais, a lógica de integridade e erro é mais complexa e pode incluir outros mecanismos de segurança.
Certifique-se de que o cliente e o servidor estejam em execução e sejam capazes de se comunicar pela rede para que a aplicação funcione corretamente.
Este relatório e manual de utilização fornecem uma visão geral dos códigos do cliente e do servidor, bem como instruções sobre como usar as aplicações. Certifique-se de ajustar a configuração de rede e o ambiente de execução conforme necessário para testar a aplicação em seu ambiente.
