# Importação de módulos necessários
import string  # Para obter caracteres alfabéticos e especiais
import random  # Para gerar números aleatórios e escolher elementos aleatórios
import re  # Para trabalhar com expressões regulares

# Definição da função gerador()
def gerador():
    padw1 = []  # Inicializa uma lista vazia para armazenar índices de tipos de caracteres
    carac = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]  # Lista de tipos de caracteres
    senha = ''  # Inicializa uma string vazia para a senha

    # Gera 14 números aleatórios que representam os tipos de caracteres
    while len(padw1) < 14:
        padw1.append(random.randint(0, len(carac) - 1))

    # Cria a senha escolhendo aleatoriamente um caractere de cada tipo
    senha = ''.join([carac[i][random.randint(0, len(carac[i]) - 1)] for i in padw1])

    return senha

# Loop infinito para gerar senhas até que uma senha válida seja encontrada
while True:
    senha = gerador()  # Chama a função gerador() para criar uma senha
    # Verifica se a senha atende aos critérios da expressão regular
    if re.fullmatch(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!])(?!.*\s).{14,}$', senha):
        print(senha)  # Se a senha for válida, imprime-a
        break  # Sai do loop infinito
