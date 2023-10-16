
import json,bcrypt,cryptography
import Gerador_senha

#Para cadastro de novo usuario deve ser criado o Json com "senhas": []

class Gerenciador():
    def __init__(self):
        self.senha = Gerador_senha.senha_f()
        with open('pass.json', 'r') as j_son:
            try:
                self.lista = json.load(j_son)
            except json.decoder.JSONDecodeError as erro:
               print(f"O json apresenta o seguinte erro:\n {erro}")

    def criar(self):
        creds = {'nome': '', 'login': ''}
        print('Digite as informações solicitadas')
        for i in creds:
            creds[i] = input(f'{i}: ')
        creds['senha'] = self.senha
        return creds

    def alterar(self, nome):
        index = [i["nome"] for i in self.lista["senhas"]]
        print(index.index(nome))
        #terminar a função de alteração

    #def remover(self):

    def salvar(self, creds):
        self.lista["senhas"].append(creds)
        create = open('pass.json', 'w')
        json.dump(self.lista, create, indent=4)



# -----------------------------------------
# Teste para criação das senhas
teste = Gerenciador()
#cadastro = teste.criar()
teste.alterar('amazon')
#teste.index()
#creds = teste.criar()
#teste.salvar(creds)
#print(teste.alterar())
#-----------------------------------------

