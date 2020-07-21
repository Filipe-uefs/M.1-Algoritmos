#Biblioteca para usar os comandos do arquivo binário
from pickle import *
#declaração da lista
tarefas_salvar=list()
#Classes usuário que realiza todas ações necessárias que o usuário fará durante o processo
class Usuario:
    #
    def __init__(self):
        self.nome= str()
        self.senha= str()
        self.menu= int()
    def name(self):
        #Abrindo o arquivo txt e adicionando o usuário
        #Obs: Como o modo de abertura está em a, ele cria o arquivo caso não exista, caso já exista ele apenas vai adicioanando em linhas posteiores
        if self.menu==1:
            with open('usuarios.txt','a') as users:
                users.write(self.nome)
                users.write("\t")
        #Confirmação de login do usuário, returna True se atender aos critérios
        else:
            with open('usuarios.txt','r') as users:
                i=0
                tamanho_arq= users.readlines()
                tamanho_arq= len(tamanho_arq)
                with open('usuarios.txt','r') as users:
                    while i<=tamanho_arq:
                        i=i+1
                        confirme= users.readline(len(self.nome))
                        if confirme==self.nome:
                            try:
                                with open(confirme, 'rb') as arq:
                                    return True
                            except IOError:
                                print()
                        
                        retira= users.readline()
                    return False
    #Usada tanto para guardar a senha no arquivo texto, quanto para verificar se a senha do usuário é correspondente ao seu cadastro
    def passoword(self):
        if self.menu==1:
            with open('usuarios.txt','a') as users:
                users.write(self.senha)
                users.write("\n")
        else:
            with open('usuarios.txt','r') as users:
                for linha in users:
                    if linha.startswith(self.nome) and linha[:-1].endswith(self.senha):
                        return True
                else:
                    return False
#Classe tarefas usada para realizar os processos
class TarefasUsers:
    def __init__(self,tarefas_salvar,user):
        self.tarefas= tarefas_salvar
        self.user=user
    def guardar(self):
        arquivo = open(self.user, 'ab')
        dump(self.tarefas, arquivo)
        arquivo.close
    def mostrar(self):
        tarefas_salvar=list()
        arquivo= open(self.user, 'rb')
        while True:
            try:
                elemento = load(arquivo)
                tarefas_salvar.append(elemento)
            except EOFError:
                break
        return tarefas_salvar

