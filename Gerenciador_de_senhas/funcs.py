
import json,bcrypt,cryptography


class Gerenciador():

    def criar(self):
        print('Digite as informações solicitadas')
        creds = {'nome': '', 'login': '', 'senha': ''}
        for i in creds:
            creds[i] = input(f'{i}: ')
        return creds

teste = Gerenciador()
cadastro = teste.criar()
print(cadastro)