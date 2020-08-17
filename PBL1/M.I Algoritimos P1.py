#/*******************************************************************************
#Autor: Filipe Pereira
#Componente Curricular: Algoritmos I
#Concluido em: 19/11/2019
#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
#******************************************************************************************/
from random import randint
import random
import string
import os
menu=1
score4=0
playerec=str()               
# Menu e seleção dos nicknames e do número de rodadas
while menu!=3:
    i=0;jogadas=11;vari1=randint(1,2);carta=0;poder=0;score1=0;score2=0;score3=0;power1=0;conf=1;fator=0
    print("Recorde atual:",score4,'\nPertence a:',playerec)
    menu=int(input("\tBem vindo ao jogo Super Trunfo YuGiOh\n(1) JOGAR\n(2) AJUDA\n(3) SAIR\n\n\n\n"))
    os.system('cls')
    if menu == 1:
      player1=str(input("Jogador 1 Digite o usuário que deseja ultilizar:\n"))
      player2=str(input("Jogador 2 Digite o usuário que deseja ultilizar:\n"))
      while jogadas>10 or jogadas<3:
             jogadas = int(input("Jogadores, escolham o número de jogadas que desejam realizar entre 3 e 10:\n"))
             os.system('cls')
      jogadas=jogadas * 2
      if score4==0:
         print('Jogadores, para jogar obedeçam as seguintes especificações, digitem o número da carta ou do atributo que deseja jogar. EX: Se quiser escolher a primeira cara, digite o número "1", isso serve para as demais ações')
         input('Pressione qualquer tecla para contiuar')
         os.system('cls')
# Definição de quem começará a partida e armazenamento dos nomes dos jogadores
      if vari1==1:
           print(player2, "você começará a partida")
           player= player2
           player0= player1
           player3=player
      elif vari1==2:
        player=player1
        player0=player2
        player3=player
        print(player1, "você começará a partida")
      while i<jogadas:

# Aleatorizando os valores dos atributos de modo que eles não sejam iguais
          atk1= randint(1,20)
          def1=atk1
          mag1=atk1
          vida=atk1
          while atk1==def1 or atk1==mag1 or atk1==vida1 or def1==mag1 or def1==vida1 or mag1==vida1:
              def1= randint(1,20)
              mag1= randint(1,20)
              vida1= randint(1,20)
          atk2= randint(1,20)
          def2=atk2
          mag2=atk2
          vida2=atk2
          while atk2==def2 or atk2==mag2 or atk2==vida2 or def2==mag2 or def2==vida2 or mag2==vida2:
               def2= randint(1,20)
               mag2= randint(1,20)
               vida2= randint(1,20)
          atk3= randint(1,20)
          def3=atk3
          mag3=atk3
          vida3=atk3
          while atk3==def3 or atk3==mag3 or atk3==vida3 or def3==mag3 or def3==vida3 or mag3==vida3:
              atk3= randint(1,20)
              def3= randint(1,20)
              mag3= randint(1,20)
              vida3= randint(1,20)

# Guardar o nome das cartas
          Mons1=[ 'Mago', 'Mistica','Minerva','Gaia','Kuriboh','Dragão','Mago','Soldier', 'Exodia']
          Mons2=[ 'Mago', 'Mistica','Minerva','Gaia','Kuriboh','Dragão','Mago','Doldier', 'Exodia']
          Mons3=[ 'Mago', 'Mistica','Minerva','Gaia','Kuriboh','Dragão','Mago','Soldier', 'Exodia']
# Jogo
          
          while conf!=0:
              print(player,'você quem está na frente do computador? Digite (0) para sim, e qualquer outro número para não')
              conf=int(input())
              os.system('cls')

# Carta
          if i%2!=0:
          	if power==1:
          		print('Atributo escolhido foi Atk ')
          	if power ==2:
          		print('Atributo escolhido foi Def')
          	if power==3:
          		print('Atributo escolhido foi Mag')
          	if power==4:
          		print('Atributo escolhido foi Vida')
          print(player,"sua vez de jogar\n\n")
          print(" "+ Mons1 [ random.randrange ( len ( Mons1 ))]," \t"+ Mons2 [ random.randrange ( len ( Mons2 ))]," \t"+ Mons3 [ random.randrange ( len ( Mons3 ))],)
          print('-------------------------------------------------')
          print('|(1)Atk:',atk1,'\t|(1)Atk:',atk2,'\t|(1)Atk:',atk3,'\t|')
          print('|(2)Def:',def1,'\t|(2)Def:',def2,'\t|(2)Def:',def3,'\t|')
          print('|(3)Mag:',mag1,'\t|(3)Mag:',mag2,'\t|(3)Mag:',mag3,'\t|')
          print('|(4)Vida:',vida1,'\t|4)Vida:',vida2,'\t|(4)Vida:',vida3,'\t|')
          print('|               |               |               |')
          print("| •Monstro 1 \t| •Monstro 2 \t| •Monstro 3","   |")
          print("| •",player,"         •",player,"       •",player)
          print(' -------------------------------------------------')
          while carta<1 or carta>3:
              carta=int(input("Escolha a carta desejada:\n"))
              if i%2!=0:
                  os.system('cls')
          while (poder<1 or poder>4) and i%2==0:
              poder=int(input("Escolha o atributo desejado:\n"))
              power=poder
          if i%2==0:
              while fator< 1 or fator>5:
                  fator=int(input("Escolha o fator de multiplicação desejado\n(1)Luz\n(2)Trevas\n(3)Fogo\n(4)Água\n(5)Vento\n"))
                  os.system('cls')

# Salvar o atributo das cartas
          if i==1 or i==2 or i==5 or i==6 or i==9:
              power1=power
              if carta==1 and power==1:
                  poder2=atk1
              elif carta==1 and power==2:
                  poder2=def1
              elif carta==1 and power==3:
                  poder2=mag1  
              elif carta==1 and power==4:
                  poder2=vida1
              elif carta==2 and power==1:
                  poder2=atk2
              elif carta==2 and power==2:
                  poder2=def2
              elif carta==2 and power==3:
                  poder2=mag2
              elif carta==2 and power==4:
                  poder2=vida2
              elif carta==3 and power==1:
                  poder2=atk3
              elif carta==3 and power==2:
                  poder2=def3
              elif carta==3 and power==3:
                  poder2=mag3
              elif carta==3 and power==4:
                  poder2=vida3
          elif i==0 or i==3 or i==4 or i==7 or i==8:
              if i!=0 and i!=4:
                  poder=power1
              if carta==1 and poder==1:
                  poder1=atk1
              elif carta==1 and poder==2:
                  poder1=def1
              elif carta==1 and poder==3:
                  poder1=mag1  
              elif carta==1 and poder==4:
                  poder1=vida1
              elif carta==2 and poder==1:
                  poder1=atk2
              elif carta==2 and poder==2:
                  poder1=def2
              elif carta==2 and poder==3:
                  poder1=mag2
              elif carta==2 and poder==4:
                  poder1=vida2
              elif carta==3 and poder==1:
                  poder1=atk3
              elif carta==3 and poder==2:
                  poder1=def3
              elif carta==3 and poder==3:
                  poder1=mag3
              elif carta==3 and poder==4:
                  poder1=vida3
              power=poder

# Ganhador da rodada
          if i%2!=0:
              poder1=poder1 * randint(1,5)
              poder2=poder2 * randint(1,5)
              if poder1>poder2:
                  score=poder1-poder2
                  score1=score1 + score
                  if vari1==1:
                      print(player3,"parabens você ganhou a rodada, dif:",score)
                  elif vari1==2:
                      print(player3,"parabens você ganhou a rodada, dif:",score)
              elif poder2>poder1:
                  score2=poder2-poder1
                  score3=score3+score2
                  
                  if vari1==1:
                      print(player0,"parabéns você ganhou a rodada, dif:",score2)
                  elif vari1==2:
                    print(player0,"parabéns você ganhou a rodada, dif:",score2)
              elif poder2==poder1:
                  print("Empate")
              print('Pontuação de', player3,'=',poder1,'Potuação de',player0,'=',poder2)
              input('Aperte Enter para contiuar')
              os.system('cls')
          i=i+1
          carta=0
          poder=0
          conf=1
          
# Ganhador da partida e novo recorde
          if i==1 or i==2 or i==5 or i==6 or i==9:
              player=player0
          elif i==3 or i==4 or i==7 or i==8:
              player=player3
          if i==jogadas:
              if score3>score1:
                  print(player0,'Parabéns, você ganhou a partida. Pontuação final:',score3)
              elif score1>score3:
                  print(player3,'Parabéns, você ganhou a partida. Pontuação final:',score1)
              else:
                  print('O jogo terminou empatado.Potuações:',score3,'/',score1)
              if score3>score1 and score3>score4:
                  score4=score3
                  playerec=player0
                  print(player0," você agora possui o novo recorde. Score:",score3)
              elif score1>score3 and score1>score4:
                  score4=score1
                  playerec=player3
                  print(player3," você agora possui o novo recorde. Score:",score1)    
              menu=int(input("Deseja jogar novamente?(1) Sim (3) Não\n"))
              os.system('cls')
              if menu==1:
                  i==0
# Ajuda
    elif menu==2:
        menu=1
        while menu<2 or menu>3:
             print("Bem vindo ao jogo Super Trunfo YuGiOh, o jogo de cartas comporta 2 jogadores e tem um minimo de 3 rodadas por partidas, ao iniicar o game os jogares escolhem seus nicknames e quantas rodadas desejam, ao final do jogo será mostrado o vencedor e seu score e se ele possuir o score maior que o recorde, ele possuirá o novo recorde")
             menu=int(input('Digite 2 para contiuar jogando e 3 para encerrar o jogo\n'))
             os.system('cls')
# Sair do jogo
    elif menu==3:
       input("Adios")
    



