import hashlib
import bcrypt
import re
from Cryptodome.Hash import MD4

def md5(hash):
    hash = hash.lower()
    with open('rockyou.txt', encoding='latin-1') as file:
        rock = file.readlines()
        p1 = hash
        for i in rock:
            pwd = hashlib.md5()
            i = i.strip('\n')
            pwd.update(i.encode('utf-8'))
            if p1 == pwd.hexdigest():
                print(f'Senha encontrada {i}')
                break


def sha1(hash):
    hash = hash.lower()
    with open('rockyou.txt', encoding='latin-1') as file:
        rock = file.readlines()
        p1 = hash
        for i in rock:
            pwd = hashlib.sha1()
            i = i.strip('\n')
            pwd.update(i.encode('utf-8'))
            if p1 == pwd.hexdigest():
                print(f'Senha encontrada {i}')
                break

def sha_salt(hash, salt):
    with open('rockyou.txt', encoding='latin-1') as file:
        rock = file.readlines()
        salt = bytes(salt, 'utf-8')
        for i in rock:
            i = i.strip('\n')
            i = bytes(i,'utf-8')
            rach = hashlib.sha256(salt + i).hexdigest()
            rach = bytes(rach,'utf-8')
            if rach == hash:
                print(i)
                break


def sha2(hash):
    hash = hash.lower()
    with open('rockyou.txt', encoding='latin-1') as file:
        rock = file.readlines()
        p1 = hash
        for i in rock:
            pwd = hashlib.sha256()
            i = i.strip('\n')
            pwd.update(i.encode('utf-8'))
            if p1 == pwd.hexdigest():
                print(f'Senha encontrada {i}')
                break


def bcript(hash):
    with open('rockyou.txt', encoding='latin-1') as file:
        rock = file.readlines()
        if salt == None:
            for i in rock:
                i = i.strip('\n')
                if re.match("^[a-z]{4}$", i):
                    i = i.encode('utf-8')
                pwd = bcrypt.checkpw(i, bytes(hash, 'utf-8'))
                if pwd == True:
                    print(i)
                    break


def md4(hash,ntlm=None):
    print('Utilize <hash>, ntlm para este tipo')
    hash = hash.lower()
    with open('rockyou.txt', encoding='latin-1') as file:
        rock = file.readlines()
        for i in rock:
            i = i.strip('\n')
            if ntlm == None:
                i = bytes(i,'utf-8')
            else:
                i = bytes(i, 'utf-16le')
            pwd = MD4.new()
            pwd.update(i)
            hashado = pwd.hexdigest()
            #print(hashado)
            #print(i)
            if hashado == hash:
                if ntlm == None:
                    print(i)
                    break
                else:
                    i = i.decode('utf-8')
                    i = i.strip(' ')
                    print(i)
                    break

#Gera uma lista mais curta para bcrypt no hashcat
# with open('rockyou.txt','r', encoding='latin-1') as file:
#     rock = file.readlines()
#     with open('rockyou6.txt','a') as rock6:
#         for i in rock:
#             if re.match("^[Aa-zZ]{6}$", i):
#                rock6.write(i)

#Tentativas e testes de gerar o bcrypt com salt
# for i in range(10):
#     salt = bcrypt.gensalt()
#     salt = b'$6$12$aReallyHardSalt6WKUTq'
#     senha = b'password123'
#     print(salt)
#     #print(senha)
#     print(bcrypt.hashpw(senha, salt),'\n\n')
#Descobrir o salt exato para iterar
# hashs = '$6$aReallyHardSalt$6WKUTqzq.UQQmrm0p/T7MPpMbGNnzXPMAXi4bJMl9be.cfi3/qxIf.hsGpS41BqMhSrHVXgMpdjS6xeKZAs02.'
# hashs2 = ''
# senha = 'password123'
# senha = bytes(senha, 'utf-8')
# for i in hashs:
#     hashs2 = hashs2 + i
#     try:
#         print(hashs2)
#         salt = bytes(hashs2, 'utf-8')
#         print(salt)
#         print(bcrypt.hashpw(senha, salt), '\n\n')
#     except ValueError as erro:
#         print(erro)
# with open('rockyou.txt', encoding='latin-1') as file:
#     rock = file.readlines()
#     for i in rock:
#         i = i.strip('\n')
#         if len(i) == 6:
#             #print(i)
#             i = bytes(i,'utf-8')
#             if bcrypt.checkpw(i,b'$2a$12$aReallyHardSalt6WKUTqzq.UQQmrm0p/T7MPpMbGNnzXPMAXi4bJMl9be.cfi3/qxIf.hsGpS41BqMhSrHVXgMpdjS6xeKZAs02.') == True:
#                 print(i)



