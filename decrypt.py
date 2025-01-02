import os
import pyaes

# Diretório onde os arquivos estão localizados
directory = '/home/kali/ransomware'

# Obter todos os arquivos no diretório com a extensão .sequestrado
encrypted_files = [f for f in os.listdir(directory) if f.endswith('.sequestrado')]

# Chave de descriptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# Processar cada arquivo criptografado
for file_name in encrypted_files:
    # Abrir o arquivo criptografado para leitura
    with open(file_name, "rb") as file:
        encrypted_data = file.read()

    # Descriptografar o conteúdo
    decrypted_data = aes.decrypt(encrypted_data)

    # Remover o arquivo criptografado
    os.remove(file_name)

    # Criar o nome do arquivo original
    new_file_name = file_name.replace('.xyz.sequestrado', '.xyz')

    # Criar o arquivo descriptografado
    with open(new_file_name, "wb") as new_file:
        new_file.write(decrypted_data)

    print(f'Arquivo {file_name} descriptografado com sucesso!')
