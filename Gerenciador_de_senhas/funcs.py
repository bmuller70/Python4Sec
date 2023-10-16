
import json,bcrypt,cryptography
import Gerador_senha



class Gerenciador():
    def __init__(self):
        self.senha = Gerador_senha.senha_f()
        with open('pass.json', 'r') as j_son:
            try:
                self.lista = json.load(j_son)
            except json.decoder.JSONDecodeError as erro:
                if erro == "Expecting value: line 1 column 1 (char 0)":
                    print('isso ai')
                else:
                    print(erro)
            # raise
            # self.lista = {}

    def criar(self):
        creds = {'nome': '', 'login': ''}
        print('Digite as informações solicitadas')
        for i in creds:
            creds[i] = input(f'{i}: ')
        creds['senha'] = self.senha
        return creds

    def salvar(self, creds):
        self.lista["senhas"].append(creds)
        create = open('pass.json', 'w')
        json.dump(self.lista, create, indent=4)



    def alterar(self):
        try:
            print(self.escrita)
        except:
            pass
    #def remover(self):

# -----------------------------------------
# Teste para criação das senhas
teste = Gerenciador()
#cadastro = teste.criar()
#teste.alterar()
creds = teste.criar()
teste.salvar(creds)
#print(teste.alterar())
#-----------------------------------------

