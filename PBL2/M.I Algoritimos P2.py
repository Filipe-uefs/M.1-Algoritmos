#biblioteca para limpar a tela
import os
#Biblioteca para construir tabela
from prettytable import PrettyTable
#Variáveis com valores atribuidos previamente pois é necessário para o inicio do programa
livre=livreendo=livrederma=1
conf=mostrar_senha=0
conf1=0
n1=n2=n3=n4=n5=n6=n7=n10=0

def os_system():
    os.system('cls')
#ConfirmaÃ§Ã£o se o  sistema deseja ser inicialializado
while conf!=1:
    conf=int(input('Bem vindo ao sistemas de senhas Oregon. Digite 1 para entrar no sistema'))
    os_system()
#Listas com as informações dos pacientes de Cardiologia
nomes_cardio=[    ]
nomes_cardio2=[  ]
hora_cardio=[]
hora_cardiores=[  ]
cardio=[  ]
cardio2=[  ]
encerracardio=[ ]
hora_atendcard=[   ]
#Listas com as informaÃ§Ãµes dos pacientes de Endocrinologia
nomes_endo=[    ]
nomes_endo2=[  ]
hora_endo=[   ]
hora_endores=[  ]
hora_atendendo=[  ]
endo=[   ]
endo2=[  ]
encerraendo=[ ]
#Listas com as informaÃ§Ãµes dos pacientes de Dermatologia
nomes_derma=[   ]
nomes_derma2=[  ]
hora_atenderma=[   ]
hora_derma=[   ]
hora_dermares=[  ]
derma=[   ]
derma2=[  ]
encerraderma=[ ]
#Listas com as informaÃ§Ãµes dos pacientes de Cardiologia Preferencial
nomes_cardiopref=[  ]
nomes_cardiopref2=[  ]
hora_cardiopref=[   ]
hora_cardioprefres=[]
cardiopref=[   ]
cardiopref2=[  ]
encerracardiopref=[  ]
hora_atendcardp= [  ]
#Listas com as informaÃ§Ãµes dos pacientes de Endocrinoliga Preferencial
nomes_endopref=[    ]
nomes_endopref2=[ ]
hora_atendendop=[   ]
hora_endopref=[   ]
hora_endoprefres=[ ]
endopref=[   ]
endopref2=[  ]
encerraendopref=[  ]
#Listas com as informaÃ§Ãµes dos pacientes de Dermatologia Preferencial
nomes_dermapref=[   ]
nomes_dermapref2=[  ]
hora_atendermap=[   ]
hora_dermapref=[   ]
hora_dermaprefres=[  ]
dermapref=[]
dermapref2=[  ]
encerradermapref=[   ]

#Menu Principal:
#Uma função contendo todas as funcionalidades do sistema e que direciona o que o usuário deseja fazer, ao escolher entre um número de 1 a 8 o programa é levado...
#a outra função para realizar a ação deseja
def menu():
    senha=0
    try:
        while senha<1 or senha>3:
            print('Digite 1 caso deseje cadastrar uma nova senha')
            print('Digite 2 para chamar paciente para o atendimento')
            print('Digite 3 caso deseje excluir alguma senha')
            print('Digite 4 para encerrar consulta ')
            print('Digite 5 para exibir fila de espera')
            print('Digite 6 para exibir pacientes atendidos no dia')
            print('Digite 7 para exibir tempo médio de espera dos pacientes')
            print('Digite 8 para exibir tempo médio de atendimento dos pacientes')
            senha=int(input())
            os_system()
            if senha==1:
                cadastrar()

            if senha==2:
                chamar()

            if senha==3:
                excluir()

            if senha==4:
                encerrar()
               
            if senha==5:
                exibir_fila()

            if senha==6:
                atendidos()

            if senha==7:
                tempo_espera()

            if senha==8:
                tempo_atendimento()
               
               
    except:
        os_system()
        return menu()
#Função cadastrar: Ao digitar 1 e selecionar está função o usuário poderá cadastrar um novo paciente, informando se ele é comum, preferencial, a hora que o paciente chegou...
#e o seu nome. As informações coletadas são adicionadas em listas de acordo com as informações passadas.    

def cadastrar():
    global n1, n2, n3, n4, n5, n6
    fila=0
    while fila<1 or fila>2 or consu<1 or consu>3:
                fila=int(input('Digite 1 para o paciente comum e 2 para o paciente especial'))
                try:
                    hora,secon= input('Digite a hora que o paciente chegou').split(':')
                except:
                    input('Voce deverÃ¡ escrever a hora do paciente do seguinte modo\nhora:minuto')
                    os_system()
                    menu1()
                consu=int(input('Digite 1 para cadastrar paciente no consultÃ³rio de Cardiologia, 2 para Endocrinologia e 3 para Demartologia'))
                nome=str(input('Digite o nome do paciente'))
                hora=int(hora)
                secon=int(secon)
               
                if fila==1 and consu==1:
                   
                    n1=n1+1
                    hora= (hora* 60) + secon
                    nomes_cardio.append(nome)
                    hora_cardio.append(hora)
                    cardio.append(n1)
                    print(n1)
                    print('Nova senha:CARD',cardio[-1])
                    print(nomes_cardio[-1])
                    print('Departamento de Cardiologia')
                   
                if fila==1 and consu==2:
                    n2=n2+1
                    hora= (hora* 60) + secon
                    nomes_endo.append(nome)
                    hora_endo.append(hora)
                    endo.append(n2)
                    print(n1)
                    print('Nova senha:ENDO',endo[-1])
                    print(nomes_endo[-1])
                    print('Departamento de Endocrinologia')
                   
                   
                if fila==1 and consu==3:
                    n3=n3+1
                    hora= (hora* 60) + secon
                    nomes_derma.append(nome)
                    hora_derma.append(hora)
                    derma.append(n3)
                    print(n1)
                    print('Nova senha:DERMA',derma[-1])
                    print(nomes_derma[-1])
                    print('Departamento de Demartologia')
                   
                if fila==2 and consu==1:
                    n4=n4+1
                    hora= (hora* 60) + secon
                    nomes_cardiopref.append(nome)
                    hora_cardiopref.append(hora)
                    cardiopref.append(n4)
                    print(n4)
                    print('Nova senha:CARDPR',cardiopref[-1])
                    print(nomes_cardiopref[-1])
                    print('Departamento de Cardiologia')
                   
                   
                if fila==2 and consu==2:
                    n5=n5+1
                    hora= (hora* 60) + secon
                    nomes_endopref.append(nome)
                    hora_endopref.append(hora)
                    endopref.append(n5)
                    print(n1)
                    print('Nova senha:ENDOP',endopref[-1])
                    print(nomes_endopref[-1])
                    print('Departamento de Endocrinologia')
                   
                if fila==2 and consu==3:
                    n6=n6+1
                    hora= (hora* 60) + secon
                    hora_dermapref.append(hora)
                    nomes_dermapref.append(nome)
                    dermapref.append(n6)
                    print('Nova senha:DERMP',dermapref[-1])
                    print(nomes_dermapref[-1])
                    print('Departamento de Demartologia')
                input()
                os_system()
                menu()
               




   




#Funão chamar, nela o é chamada a próxima senha a ser chamadad de acordo com o consultório desejado e o atendente informa o horário de chegada
def chamar():
  # 3 variaveis no escopo de globais pois serâo utilizadas em outras partes do programa
    global livre, livreendo, livrederma
    cardio4=endo4=derma4=0
    cardio5=endo5=derma5=1
           
    chamar1=int(input('Digite 1 para chamar paciente para ser atendido no consultÃ³rio de Cardiologia, 2 para Endocrinologia e 3 para Demartologia'))
    print(livrederma)
    if chamar1==1:
        if livre==1:
            if len(cardio)==0:
                cardio3=999999999999999999
            else:
                cardio3=cardio[0]
            if len(cardio)==0 and len(cardiopref)==0:
                print('Sem senhas cadastradas neste consultório')
                cardio5=0
               
            elif len(cardiopref)==0 or cardio3<cardiopref[0]:
                print('Próxima senha a ser chamada')
                print('CARD',cardio[0])
                print(nomes_cardio[0])
                print('Departamento de Cardiologia')
           
                hora_cardiores.append(hora_cardio[0])
                hora_cardio.pop(0)
                cardio2.append(cardio[0])
                nomes_cardio2.append(nomes_cardio[0])
                cardio.pop(0)
                nomes_cardio.pop(0)
                cardio4=1
            elif len(cardiopref)>0:
                print('Próxima senha a ser chamada')
                print('CARDPR',cardiopref[0])
                print(nomes_cardiopref[0])
                print('Departamento de Cardiologia')

                hora_cardioprefres.append(hora_cardiopref[0])
                hora_cardiopref.pop(0)
                cardiopref2.append(cardiopref[0])
                cardiopref.pop(0)
                nomes_cardiopref2.append(nomes_cardiopref[0])
                nomes_cardiopref.pop(0)
                cardio4=1
           
               
    elif chamar1==2:
        if livreendo==1:
            if len(endo)==0:
                endo3=999999999999999999
            else:
                endo3=endo[0]
            if len(endo)==0 and len(endopref)==0:
                print('Sem senhas cadastradas neste consultório')
                endo5=0
               
               
            elif len(endopref)==0 or endo3<endopref[0]:
                print('Próxima senha a ser chamada')
                print('ENDO',endo[0])
                print(nomes_endo[0])
                print('Departamento de Endocrinologia')
           
                hora_endores.append(hora_endo[0])
                hora_endo.pop(0)
                endo2.append(endo[0])
                nomes_endo2.append(nomes_endo[0])
                endo.pop(0)
                nomes_endo.pop(0)
                endo4=1
            elif len(endopref)>0:
                print('Próxima senha a ser chamada')
                print('ENDOP',endopref[0])
                print(nomes_endopref[0])
                print('Departamento de Endocrinologia')

               
                hora_endoprefres.append(hora_endopref[0])
                hora_endopref.pop(0)
                endopref2.append(endopref[0])
                nomes_endopref2.append(nomes_endopref[0])
                endopref.pop(0)
                nomes_endopref.pop(0)
                endo4=1
           
       
    elif chamar1==3:
        if livrederma==1:
            if len(derma)==0:
                derma3=999999999999999999
               
            else:
                derma3=derma[0]
            if len(derma)==0 and len(dermapref)==0:
                print('Sem senhas cadastradas neste consultório')
                derma5=0
               
            elif len(dermapref)==0 or derma3<dermapref[0]:
                print('Próxima senha a ser chamada')
                print('DERMA',derma[0])
                print(nomes_derma[0])
                print('Departamento de Dermatologia')
           
                hora_dermares.append(hora_derma[0])
                hora_derma.pop(0)
                derma2.append(derma[0])
                nomes_derma2.append(nomes_derma[0])
                derma.pop(0)
                nomes_derma.pop(0)
                derma4=1
            elif len(dermapref)>0:
                print('Próxima senha a ser chamada')
                print('DERMAP',dermapref[0])
                print(nomes_dermapref[0])
                print('Departamento de Dermatologia')

               
                hora_dermaprefres.append(hora_dermapref[0])
                hora_dermapref.pop(0)
                dermapref2.append(dermapref[0])
                nomes_dermapref2.append(nomes_dermapref[0])
                dermapref.pop(0)
                nomes_dermapref.pop(0)
                derma4=1
   
    if livre==1 or livreendo==1 or livrederma==1:
       
        if  cardio4==1 or endo4==1 or derma4==1:
            hora1,hora2= input('Digite a hora que o atendimento está começando').split(':')
            hora1=int(hora1)
            hora2=int(hora2)
            hora1= (hora1 * 60) + hora2
            if chamar1==1:
                livre=0
                print('Digite 1 caso o paciente seja comum e 2 caso seja preferencial')
                hora_deci=int(input())
                if hora_deci==1:
                    hora_atendcard.append(hora1)
                else:
                    hora_atendcardp.append(hora1)
               
            if chamar1==2:
                livreendo=0
                print('Digite 1 caso o paciente seja comum e 2 caso seja preferencial')
                hora_deci=int(input())
                if hora_deci==1:
                    hora_atendendo.append(hora1)
                else:
                    hora_atendendop.append(hora1)
            if chamar1==3:
                livrederma=0
                print('Digite 1 caso o paciente seja comum e 2 caso seja preferencial')
                hora_deci=int(input())
                if hora_deci==1:
                    hora_atenderma.append(hora1)
                else:
                    hora_atendermap.append(hora1)
               
        else:
            if endo5==1 and cardio5==1 and derma5==1:
                print('Consultório cheio')
    if livre==0 and livreendo==0 and livrederma==0 :
        print('Consultório cheio')
         
           
           
           
   
    menu()

#Função exlcuir, nela o funcionário poderá excluir algum paciente da lista informando, o consultório, se comum ou preferencial e o número da senha do paciente  
def excluir():
    excluir= int(input('Digite 1 para caso deseje excluir alguma senha do derpatamento de Cardiologia, 2 para endocrinologia, e 3 para dermatologia'))
    excluir1= int(input('Digite 1 caso seja comum,2 para preferencial'))
    end= int(input('Digite o numero da senha'))
    if excluir==1 and excluir1==1:
        hora_cardio.pop(end-1)
        cardio.pop(end-1)
        nomes_cardio.pop(end-1)
    if excluir==1 and excluir1==2:
        hora_cardiopref.pop(end-1)
        cardio.pref.pop(end-1)
        nomes_cardiopref.pop(end-1)
    if excluir==2 and excluir1==1:
        hora_endo.pop(end-1)
        endo.pop(end-1)
        nomes_endo.pop(end-1)
    if excluir==2 and excluir1==2:
        hora_endopref.pop(end-1)
        endo_pref.pop(end-1)
        nomes_endo.pop(end-1)
    if excluir==3 and excluir1==1:
        hora_derma.pop(end-1)
        derma.pop(end-1)
        nomes_derma.pop(end-1)
    if excluir==3 and excluir1==2:
        hora_dermapref.pop(end-1)
        dermapref.pop(end-1)
        nomes_dermapref.pop(end-1)
    menu()

#Função encerrar, para liberar a sala para chamar novos pacientes é necessário encerrar a cunsulta que está sendo realizada. Nesta função será informado o consultório, preferencial ou comum, e horário de término da consulta
def encerrar():
    # variaveis globais 
    global livre, livreendo, livrederma
    encerramento= int(input('Digite 1 para caso deseje encerrar consulta do derpatamento de Cardiologia, 2 para endocrinologia, e 3 para dermatologia'))
    encerramento1= int(input('Digite 1 caso o paciente atendido seja comum,2 para preferencial'))
    encerramentohora, encerramentominuto= input('Digite a hora que o atendimento foi finalizado').split(':')
    encerramentohora=int(encerramentohora)
    encerramentominuto=int(encerramentominuto)
    encerramentohora= (encerramentohora * 60) + encerramentominuto
    if encerramento==1 and encerramento1==1:
        encerracardio.append(encerramentohora)
        livre=1
        print(encerracardio)
       
       
    if encerramento==2 and encerramento1==1:
        encerraendo.append(encerramentohora)
        livreendo=1
       
    if encerramento==3 and encerramento1==1:
        encerraderma.append(encerramentohora)
        livrederma=1
       
    if encerramento==1 and encerramento1==2:
        encerracardiopref.append(encerramentohora)
        livre=1
       
    if encerramento==2 and encerramento1==2:
        encerraendopref.append(encerramentohora)
        livreendo=1
       
    if encerramento==3 and encerramento1==2:
        encerradermapref.append(encerramentohora)
        livrederma=1

#Função cujo objetivo é informar a média do tempo de espera dos pacientes, aqui é possivel saber a média geral de todos os pacientes atendidos no dia, assim como saber a média por consultório e por espeficidade(comum ou preferencial)
def tempo_espera():
  # variaveis pré definadas  para iniciar a execução da funão
    espera_card=0
    espera_cardp=0
    espera_endo=0
    espera_endop=0
    espera_derma=0
    x2=x3=x4=x5=x6=x7=0
    espera_dermap=0




#Cardiologia comum
    print("CARDIOLOGIA")
    x2= len(cardio2)
    for i in range(x2):
        x1= hora_atendcard[i] - hora_cardiores[i]
        espera_card= espera_card + x1
    if x2>0:
         print("Tempo de espera comuns/cardiologia", espera_card/x2, "minutos")
    else:
        print("Sem informações no sistema comum/cardiologia")
       
#Cardiologia preferencial
    x3= len(cardiopref2)
    for f in range(x3):
        x1= hora_atendcardp[f] - hora_cardioprefres[f]
        espera_cardp= espera_cardp + x1
    if x3>0:
        print("Tempo de espera preferencial/cardiologia", espera_cardp/x3,"minutos")
    else:
        print("Sem informações no sistema preferencial/cardiologia")
    if (x2+x3)>0:
        print("Tempo geral de espera cardiologia", (espera_card+espera_cardp)/(x2+x3),"minutos\n\n")
    else:
        print("Sem informações sobre o departamento de cardiologia\n\n")

    print("ENDOCRINOLOGIA")
       
#Endocrinologia comum
    x4= len(endo2)
    for y in range(x4):
        x1= hora_atendendo[y] - hora_endores[y]
        espera_endo= espera_endo + x1
    if x4>0:
        print("Tempo de espera comum/endocrinologia", espera_endo/x4,"minutos")
    else:
        print("Sem informações no sistema comum/endocrinologia")
   
     
#Endocrinologia preferencial
    x5= len(endopref2)
    for h in range(x5):
        x1= hora_atendendop[h] - hora_endoprefres[h]
        espera_endop= espera_endop + x1
    if x5>0:
        print("Tempo de espera preferencial/endocrinologia", espera_endop/x5,"miinutos")
    else:
        print("Sem informações no sistema preferencial/endocrinologia")
       
    if (x4+x5)>0:
         
        print("Tempo geral de espera endocrinologia", (espera_endo+espera_endop)/(x4+x5),"minutos\n\n")
    else:
        print("Sem informações sobre o departamento de endocrinologia\n\n")
       
       

    print("DERMATOLOGIA")    
       
#Dermatologia comum
    x6= len(derma2)
    for g in range(x6):
        x1= hora_atenderma[g] - hora_dermares[g]
        espera_derma= espera_derma + x1
    if x6>0:
        print("Tempo de espera comum/dermatologia", espera_derma/x6, "minutos")
    else:
        print("Sem informações no sistema comum/dermatologia")
       

#Dermatologia preferencial
    x7= len(dermapref2)
    for t in range(x7):
        x1= hora_atendermap[t] - hora_dermaprefres[t]
        espera_dermap= espera_dermap + x1
    if x7>0:
        print("Tempo de espera preferencial", espera_dermap/x7, "minuto")
    else:
        print("Sem informações no sistema comum/cardiologia")
    if (x6+x7)>0:
         
        print("Tempo geral de espera endocrinologia", (espera_derma+espera_dermap)/(x6+x7),"minutos\n\n")
    else:
        print("Sem informações sobre o departamento de endocrinologia\n\n")
#Comum
    print("COMUM")
    if (x2+x4+x6)>0:
        print("Tempo de espera dos comuns\n\n", (espera_derma+espera_endo+espera_card)/(x2+x4+x6))
    else:
        print("Sem informações sobre pacientes comuns\n\n")
#Preferencial
    print("PREFERENCIAL")
    if (x3+x5+x7)>0:
        print("Tempo de espera dos preferenciais\n\n", (espera_dermap+espera_endop+espera_cardp)/(x3+x5+x7))
    else:
        print("Sem informações sobre pacientes comuns\n\n")
#Geral
    print("GERAL")
    if (x3+x5+x7+x2+x4+x6)>0:
        print("Tempo de espera dos preferenciais\n\n", (espera_dermap+espera_endop+espera_cardp+espera_derma+espera_endo+espera_card)/(x3+x5+x7+x2+x4+x6))
    else:
        print("Sem informações sobre nenhum paciente\n\n")
   
   

def tempo_atendimento():
   # Váriaveis pré definadas para auxiliar o algoritimo
    at_card=0
    atp_cardp=0
    at_endo=0
    at_endop=0
    at_derma=0
    x2=x3=x4=x5=x6=x7=0
    at_dermap=0

#Cardiologia comum
    print("CARDIOLOGIA")
    print(encerracardio)
    x2= len(cardio2)
    for i in range(x2):
        x1= encerracardio[i] - hora_atendcard[i]
        at_card= at_card + x1
    if x2>0:
         print("Tempo de atendimento comuns/cardiologia", at_card/x2, "minutos")
    else:
        print("Sem informações no sistema comum/cardiologia")
       
#Cardiologia preferencial
    x3= len(cardiopref2)
    for f in range(x3):
        x1= encerracardiopref[f] - hora_atendcardp[f]
        atp_cardp= atp_cardp + x1
    if x3>0:
        print("Tempo de atendimento preferencial/cardiologia", atp_cardp/x3,"minutos")
    else:
        print("Sem informações no sistema preferencial/cardiologia")
    if (x2+x3)>0:
        print("Tempo geral de atendimento cardiologia", (at_card+atp_cardp)/(x2+x3),"minutos\n\n")
    else:
        print("Sem informações sobre o departamento de cardiologia\n\n")

    print("ENDOCRINOLOGIA")
       
#Endocrinologia comum
    x4= len(endo2)
    for y in range(x4):
        x1= encerraendo[y] - hora_atendendo[y]
        at_endo= at_endo + x1
    if x4>0:
        print("Tempo de atendimento comum/endocrinologia", at_endo/x4,"minutos")
    else:
        print("Sem informações no sistema comum/endocrinologia")
   
     
#Endocrinologia preferencial
    x5= len(endopref2)
    for h in range(x5):
        x1= encerraendopref[h] - hora_atendendop[h]
        at_endop= at_endop + x1
    if x5>0:
        print("Tempo de atendimento preferencial/endocrinologia", at_endop/x5,"miinutos")
    else:
        print("Sem informações no sistema preferencial/endocrinologia")
       
    if (x4+x5)>0:
         
        print("Tempo geral de atendimento endocrinologia", (at_endo+at_endop)/(x4+x5),"minutos\n\n")
    else:
        print("Sem informações sobre o departamento de endocrinologia\n\n")
       
       

    print("DERMATOLOGIA")    
       
#Dermatologia comum
    x6= len(derma2)
    for g in range(x6):
        x1= encerraderma[g] - hora_atenderma[g]
        at_derma= at_derma + x1
    if x6>0:
        print("Tempo de atendimento comum/dermatologia", at_derma/x6, "minutos")
    else:
        print("Sem informações no sistema comum/dermatologia")
       

#Dermatologia preferencial
    x7= len(dermapref2)
    for t in range(x7):
        x1= encerradermapref[t] - hora_atendermap[t]
        at_dermap= at_dermap + x1
    if x7>0:
        print("Tempo de atendimento preferencial", at_dermap/x7, "minuto")
    else:
        print("Sem informações no sistema comum/cardiologia")
    if (x6+x7)>0:
         
        print("Tempo geral de atendimento endocrinologia", (at_derma+at_dermap)/(x6+x7),"minutos\n\n")
    else:
        print("Sem informações sobre o departamento de endocrinologia\n\n")
#Comum
    print("COMUM")
    if (x2+x4+x6)>0:
        print("Tempo de atendimento dos comuns\n\n", (at_derma+at_endo+at_card)/(x2+x4+x6))
    else:
        print("Sem informações sobre pacientes comuns\n\n")
#Preferencial
    print("PREFERENCIAL")
    if (x3+x5+x7)>0:
        print("Tempo de atendimento dos preferenciais\n\n", (at_dermap+at_endop+atp_cardp)/(x3+x5+x7))
    else:
        print("Sem informações sobre pacientes comuns\n\n")
#Geral
    print("GERAL")
    if (x3+x5+x7+x2+x4+x6)>0:
        print("Tempo de atendimento dos preferenciais\n\n", (at_dermap+at_endop+atp_cardp+at_derma+at_endo+at_card)/(x3+x5+x7+x2+x4+x6))
    else:
        print("Sem informações sobre nenhum paciente\n\n")
# Função Exibir fila, nela é usada a biblioteca pretty table para organizar as informações em forma de tabela. Deste modo, para o usuário obter informações sobre o consolutório será necessário informar o horário atual, assim obetendo uma tabela com as informações dos pacientes em espera.
def exibir_fila():

  hora_agora, hora_agr= input("Digite a hora atual").split(":")
  hora_agora= int(hora_agora)
  hora_agr= int(hora_agr)
  hora_agora= (hora_agora * 60) + hora_agr
  tabela=len(cardio)
  cardt = PrettyTable()
  cardt.field_names = ["Senha CARD","Nome", "Status","Tempo de espera"]
  for i in range(tabela):
    cardt.add_row([cardio[i],nomes_cardio[i],"Em espera",hora_agora-hora_cardio[i]])
         

  print(cardt)
#Cardiologia preferencial
  tabela=len(cardiopref)
  cardtp = PrettyTable()
  cardtp.field_names = ["Senha CARD","Nome", "Status","Tempo de espera"]
  for i in range(tabela):
    cardtp.add_row([cardiopref[i],nomes_cardiopref[i],"Em espera",hora_agora-hora_cardiopref[i]])
         

  print(cardtp)

  #Endocrionologia COMUM
  tabela=len(endo)
  endot = PrettyTable()
  endot.field_names = ["Senha CARD","Nome", "Status","Tempo de espera"]
  for i in range(tabela):
    endot.add_row([endo[i],nomes_endo[i],"Em espera",hora_agora-hora_endo[i]])
         

  print(endot)
  #Endocrinologia preferencial

  tabela=len(endo)
  endotp = PrettyTable()
  endotp.field_names = ["Senha CARD","Nome", "Status","Tempo de espera"]
  for i in range(tabela):
    endotp.add_row([endopref[i],nomes_endopref[i],"Em espera",hora_agora-hora_endopref[i]])
         

  print(endotp)
  #Demartologia
  tabela=len(derma)
  dermat = PrettyTable()
  dermat.field_names = ["Senha DERMA","Nome", "Status","Tempo de espera"]
  for i in range(tabela):
    dermat.add_row([derma[i],nomes_derma[i],"Em espera",hora_agora-hora_derma[i]])
         

  print(dermat)
  #Demartologia preferencial
  tabela=len(dermapref)
  dermatp = PrettyTable()
  dermatp.field_names = ["Senha DERMAP","Nome", "Status","Tempo de espera"]
  for i in range(tabela):
    dermatp.add_row([dermapref[i],nomes_dermapref[i],"Em espera",hora_agora-hora_dermapref[i]])
         

  print(dermatp)
# Nesta é informado o tempo de atendimento em forma de tabela, para isto foi necessário a função pretty table e ir adicionando informações em cada coluna afim de que ao final o usuário recebe em forma de tabela as informações de cada paciente.
def atendidos ():
#Cardiologia comum
  tabela=len(cardio2)
  cardt = PrettyTable()
  cardt.field_names = ["Nome", "Tempo de espera","Tempo de atendimento", "Consultório", "Médico do consultório"]
  for i in range(tabela):
    cardt.add_row([nomes_cardio2[i],hora_atendcard[i] - hora_cardiores[i],encerracardio[i] - hora_atendcard[i], "Cardiologia", "DR Maria do Carmo Silva"])
  print(cardt)
  #Cardiologia preferencial
  tabela=len(cardiopref2)
  cardtp = PrettyTable()
  cardtp.field_names = ["Nome", "Tempo de espera","Tempo de atendimento", "Consultório", "Médico do consultório"]
  for f in range(tabela):
    cardtp.add_row([nomes_cardiopref2[f],hora_atendcardp[f] - hora_cardioprefres[f],encerracardiopref[f] - hora_atendcardp[f] , "Cardiologia", "Maria do Carmo Silva"])
  print(cardtp)

  #Endo comum
  tabela=len(endo2)
  endot = PrettyTable()
  endot.field_names = ["Nome", "Tempo de espera","Tempo de atendimento", "Consultório", "Médico do consultório"]
  for i in range(tabela):
    endot.add_row([nomes_endo2[i],hora_atendendo[i] - hora_endores[i],encerraendo[i] - hora_atendendo[i], "Endocrinologia", "DR. Fernando Santos"])
  print(endot)
  #Endo preferencial
  tabela=len(endopref2)
  endotp = PrettyTable()
  endotp.field_names = ["Nome", "Tempo de espera","Tempo de atendimento", "Consultório", "Médico do consultório"]
  for g in range(tabela):
    endotp.add_row([nomes_endopref2[g],hora_atendendop[g] - hora_endoprefres[g],encerraendopref[g] - hora_atendendop[g], "Endocrinologia", "DR. Fernando Santos"])
  print(endotp)
  #Dermatologia comum

  tabela=len(derma2)
  dermat = PrettyTable()
  dermat.field_names = ["Nome", "Tempo de espera","Tempo de atendimento", "Consultório", "Médico do consultório"]
  for s in range(tabela):
    dermat.add_row([nomes_derma2[s],hora_atenderma[s] - hora_dermares[s],encerraderma[s] - hora_atenderma[s], "Dermatologia", "DR Silvia Melo"])
  print(dermat)
  #Demartologia preferencial
  tabela=len(dermapref2)
  dermatp = PrettyTable()
  dermatp.field_names = ["Nome", "Tempo de espera","Tempo de atendimento", "Consultório", "Médico do consultório"]
  for u in range(tabela):
    dermatp.add_row([nomes_dermapref2[u],hora_atendermap[u] - hora_dermaprefres[u],encerradermapref[u] - hora_atendermap[u], "Dermatologia", "DR Silvia Melo"])
  print(dermatp)




         
menu()
