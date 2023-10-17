
import json,bcrypt,cryptography
import Gerador_senha

#Para cadastro de novo usuario deve ser criado o Json com "senhas": []

class Gerenciador():
    def __init__(self):
        self.senha = Gerador_senha.senha_f()
        with open('pass.json', 'r') as j_son: #Carrega o json para dentro da variavel self.lista
            try:
                self.lista = json.load(j_son)
            except json.decoder.JSONDecodeError as erro:
               print(f"O json apresenta o seguinte erro:\n {erro}")

    def criar(self): #Cria um dicionario com as novas credencias
        creds = {'nome': '', 'login': ''}
        print('Digite as informações solicitadas')
        for i in creds:
            creds[i] = input(f'{i}: ')
        creds['senha'] = self.senha
        self.lista["senhas"].append(creds)

    def alterar(self, nome): #Altera credenciais
        index = [i["nome"] for i in self.lista["senhas"]]
        item = index.index(nome)
        alteracao = int(input('Selecione a alteração desejada \n 1 - Alterar senha \n 2 - Alterar Login \n 3 - Alterar nome \n Insira o numero da opção: '))
        if alteracao not in (1,2,3):
            print('Opção invalida')
        else:
            if alteracao == 1:
                n_senha = input('Digite a nova senha: ')
                try:
                    self.lista["senhas"][item]["senha"] = n_senha
                except:
                    raise
            elif alteracao == 2:
                n_login = input('Digite o novo login: ')
                try:
                    self.lista["senhas"][item]["login"] = n_login
                except:
                    raise

            elif alteracao == 3:
                n_nome = input('Digite a novo nome: ')
                try:
                    self.lista["senhas"][item]["nome"] = n_nome
                except:
                    raise

    def remover(self):
        pass





    def salvar(self): #Reescreve no json a variavel self.lista
        create = open('pass.json', 'w')
        json.dump(self.lista, create, indent=4)



# -----------------------------------------
# Teste para criação das senhas
teste = Gerenciador()
#cadastro = teste.criar()
teste.alterar('teste2')
#teste.criar()
teste.salvar()
#teste.index()
#creds = teste.criar()
#teste.salvar(creds)
#print(teste.alterar())
#-----------------------------------------

