tamanho_arquivo = float(input('Informe o tamanho do arquivo (em MB): '))
velocidade_transferencia = float(input('Informe a velocidade de conexao (em Mbps): '))

tamanho_bits = tamanho_arquivo * 1024 * 1024 * 8
tempo_segundos = tamanho_bits / (velocidade_transferencia * 1024 * 1024)
tempo_minutos = tempo_segundos / 60

print(f'O tempo aproximado de download é de {round(tempo_minutos, 2)} minutos')