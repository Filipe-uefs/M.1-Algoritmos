#/*******************************************************************************
#Autor: Filipe Pereira da Silva
#Componente Curricular: Algoritmos I
#Concluido em: 28/03/2020
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
#******************************************************************************************/




#Biblioteca para tranfomrar a senha do usuario em um hash
import hashlib
#Biblioteca para limpar a tela
import os
#Bibliotecas contendo as classes usuário e tarefas
from users import Usuario
from users import TarefasUsers
#Biblioteca usada para utlizar os comandos do arquivo binário
from pickle import *
#Biblioteca para importar tabelas
from prettytable import PrettyTable
#lista e variáveis declaradas previamente para não ocorrer erro de não definição
tarefas=tarefas_=[]
tarefas_salvar= []
n1=n2=n3=0
#print para mostrar bem vindo ao sistema
print(' -------------------------------------------------------------')
print('|          Bem vindo ao sistema de tarefas, Lipos             |')
print(' -------------------------------------------------------------')
#Menu que inicializará o sistema de tarefas, nela poderá ser possivel cadastrar novos usuários, fazer login e sair
def menu():
    try:
        menu_ini=0
        while menu_ini<1 or menu_ini>3:
            print('Cadastrar novo usuário (1)')
            print('Realizar Login (2)')
            print('Sair (3)')
            menu_ini=int(input())
            os.system('cls')
            
        if menu_ini==1:
            cadastrar_user(menu_ini)
        elif menu_ini==2:
            entrar(menu_ini)
        else:
            print('programa encerrado')
    except:
        menu()
#Função cadastrar menu, o usuário fornece o username que deseja utilizar e sua senha, a senha é tranformada em um hash atráves da biblioteca hashilib
#O usuário é um objeto instanticado que tem as caracterisiticas nome e senha
def cadastrar_user(menu_ini):
    os.system('cls')
    u= Usuario()
    u.nome=input('Novo nome do usuário\n')
    u.senha=input('Nova senha do usuário\n')
#Verifica se existe um arquivo binário aberto com este nome usado 'rb', caso não, ele abre o arquivo usando o metódo 'wb'
    try:
        with open(u.nome,'rb') as verificacao:
            print('Nome já existente, tente novamente')
            cadastrar_user(menu_ini)
    except IOError:
        u.menu= menu_ini
        has= hashlib.md5(u.senha.encode())
        u.senha=has.hexdigest()
        u.name()
        u.passoword()
        input('Cadastro realizado com sucesso, aperte enter para contiuar')
        with open(u.nome, 'wb') as cadastro:
            menu()

#Função entrar: Nela é coletado o login e a senha. Essas informações são passadas como parametro para a classe Usuario
#que verifica se as informações passadas estão corretas, caso sim, ele retorna True ou False
#Cabe a ressalva que ao enviar a senha como parametro, será enviado o hash da senha digitada, pois o que ficou salvou no arquivo txt, foi seu hash


#Função para logar ao sistema
def entrar(menu_ini):
    os.system('cls')
    u= Usuario()
    u.nome= input('login\n')
    os.system('cls')
    u.senha= input('Senha\n')
    u.menu= menu_ini
    has1= hashlib.md5(u.senha.encode())
    u.senha=has1.hexdigest()
    entrar_nome= u.name()
    if entrar_nome== True:
        entrar_senha=u.passoword()
        if entrar_senha== True:
           sistema(u.nome)
        else:
           print('Senha incorreta')
    
    else:
        print('Nome do usuário inexistente ou invalidado, tente novamente')
    input('Aperte enter para contiuar')
    os.system('cls')
    entrar(menu_ini)
    
#Sistama logado
def sistema(user):
    
    while True:
        #Menu com as opções para usuário escolher o que deseja fazer
        os.system('cls')
        print('Você está logado no sistema ')
        print('Cadastrar nova Tarefa       (1)')
        print('Visualizar Tarefas          (2)')
        print('Alterar Tarefas             (3)')
        print('Excluir Tarefa              (4)')
        print('Sair do sistema             (5)')
        try:
            system= int(input())
        except:
            sistema(user)
        if system<1 or system>5 or system=='':
            print('ação invalida')
        else:
            break
    #Estruturas de seleção que direcionam para onde programa deve ir
    if system==1:
        cadastrar(user)
    elif system==2:
        c=TarefasUsers(tarefas_salvar,user)
        mostrar_taf= c.mostrar()
        while True:
            quantidade= len(mostrar_taf)
            table= tabela_taf(user, mostrar_taf)
            break
        if len(mostrar_taf)==0:
            print('Você não cadastrou nenhuma tarefa')
        else:
            print(table)
        input('Aperte enter para continuar')
        sistema(user)
    elif system==3:
        alterar(user)
        
    elif system==4:
        excluir(user)
    elif system==5:
        os.system('cls')
        menu()
#Função cadastrar:
#
def cadastrar(user):
    tarefas_=list()
    titulo= str(input('Digite o titulo da sua tarefa'))
    descri= str(input('Escreva a descrição '))
    n1=n2=n3=0
    
    while True:
        try:
            prio= int(input('informe a prioridade da tarefa, entre Alta(1), Média(2) e baixa(3)'))
            if prio>=1 or prio<=3:
                break
        except:
            True
    try:
        with open(user, 'rb') as arq:
            while True:
                try:
                    elemento = load(arq)
                    tarefas_.append(elemento)
                    
                except EOFError:
                    i= len(tarefas_)
                    for x in range(i):
                        if tarefas_[x][0][2]==1:
                            n1= n1+1
                    for x in range(i):
                        if tarefas_[x][0][2]==2:
                            n2= n2+1
                    for x in range(i):
                        if tarefas_[x][0][2]==3:
                            n3= n3+1
                    if prio==3:
                       i_d=n3+1
                    elif prio==2:
                       i_d= n2+1
                    else:
                       i_d= n1+1
                    print(i_d)
                    break
    except IOError:
        i_d= 1
    tarefas=[]
    tarefas_salvar=[]
    tarefas.append(titulo)
    tarefas.append(descri)
    tarefas.append(prio)
    tarefas.append(i_d)
    tarefas_salvar.append(tarefas)
   
    c= TarefasUsers(tarefas_salvar,user)
    c.guardar()
    sistema(user)

#Função alterar:
#
def alterar(user):
    posicao=0
    c=TarefasUsers(tarefas_salvar,user)
    mostrar_taf= c.mostrar()
    while True:
        quantidade= len(mostrar_taf)
        table= tabela_taf(user, mostrar_taf)
        if len(mostrar_taf)==0:
            print('Você não cadastrou nenhuma tarefa')
            input()
            sistema(user)
        
        print(table)
        while True:
            try:
                print('Digite uma ID entre acima')
                n= int(input())
                n1=0
                while n1<1 or n1>3:
                    n1=int(input('Digite a prioridade (1)alta (2)media (3)baixa'))
                break
            except:
                print('Erro na insersação de dados')
                input('aperte enter para conituar')
        for x in range(quantidade):
            if mostrar_taf[x][0][2]==n1 and mostrar_taf[x][0][3]==n:
                posicao=x
                title= str(input('Novo titulo'))
                descri= str(input('Nova descrição'))
                while True:
                    try:
                        prioridade=0
                        while prioridade<1 or prioridade>3:
                            prioridade= int(input('Digite a nova prioridade alta(1), media(2), baixa(3)'))
                            if prioridade!=n1:
                                mostrar_taf[posicao][0][3]=mostrar_taf[posicao][0][3]+1
                        break
                    except:
                        print('Erro na insersação de dados')
                        input('aperte enter para conituar')
                
                mostrar_taf[posicao][0][0]= title
                mostrar_taf[posicao][0][1]= descri
                mostrar_taf[posicao][0][2]= prioridade
                input('Aperte enter para contiuar')
                with open(user,'wb') as alteracao:
                    for x in range(len(mostrar_taf)):
                        dump(mostrar_taf[x],alteracao)
                sistema(user)
            nao_encontrado= 0
            
        if nao_encontrado==0:
            input('Nenhuma tarefa encontrada, digite enter para continuar')
            sistema(user)
                    
                            
                          
                            
        break
        
                                       
                                
                       
    
#Função que mostra a tabela com as atividade de cada usuário. É usado a biblioteca PrettyTable, assim os valores são inserdios em seus campos
def tabela_taf(user, tarefas_):
    tarefas_.sort()
    alta=baixa=media=0
    quantidade= len(tarefas_)
    tabela_altera= PrettyTable()
    tabela_altera.field_names= ["Titulo","Descrição","Prioridade","ID"]
    for x in range(quantidade):
        if tarefas_[x][0][2]==1:
            alta= alta+1
            tabela_altera.add_row([tarefas_[x][0][0],tarefas_[x][0][1],"ALTA",tarefas_[x][0][3]])
    for x in range(quantidade):
        if tarefas_[x][0][2]==2:
            tabela_altera.add_row([tarefas_[x][0][0],tarefas_[x][0][1],"MEDIA",tarefas_[x][0][3]])
            media=media+1
    for x in range(quantidade):
        if tarefas_[x][0][2]==3:
            tabela_altera.add_row([tarefas_[x][0][0],tarefas_[x][0][1],"BAIXA",tarefas_[x][0][3]])
            baixa=baixa+1
        
    
    return tabela_altera
#Função excluir:
def excluir(user):
    c=TarefasUsers(tarefas_salvar,user)
    mostrar_taf= c.mostrar()
    
    while True:
        #Mostra a tabela
        quantidade= len(mostrar_taf)
        table= tabela_taf(user, mostrar_taf)
        if len(mostrar_taf)==0:
            print('Você não cadastrou nenhuma tarefa')
            input()
            sistema(user)
        
        print(table)
        while True:
            try:
                print('Digite uma ID entre acima')
                n= int(input())
                n1=0
                while n1<1 or n1>3:
                    n1=int(input('Digite a prioridade (1)alta (2)media (3)baixa'))
                break
            except:
                print('Erro na insersação de dados')
                input('aperte enter para conituar')
        #Procura a tarefa de acordo com a ID e com a prioridade, quando achada, exclui a usando a função del, caso não encontre, o sistema volta ao menu 
        for x in range(quantidade):
        
            if mostrar_taf[x][0][2]==n1 and mostrar_taf[x][0][3]==n:
                
                del(mostrar_taf[x])
                nao_encontrado= 1
                input('Aperte enter para contiuar')
                with open(user,'wb') as alteracao:
                    for x in range(len(mostrar_taf)):
                        dump(mostrar_taf[x],alteracao)
                sistema(user)
            else:
                nao_encontrado= 0
        if nao_encontrado==0:
            print('Nenhuma tarefa com essa carcteristica encontrada')
            input('Aperte enter para contiuar')
            sistema(user)
                                              
        break
#Se não existir mais elementos dentro da lista presente no arquivo binário do usuário, o sistema cria novamente este arquivo em branco
    if len(mostrar_taf)==0:
        with open(user,'wb') as alteracao:
            print()
        sistema(user)
            
#inicializa o código
menu()

