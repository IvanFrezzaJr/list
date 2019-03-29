import os
import time

# Mensagem simples
def message(msg):
    clear()
    print(msg)
    time.sleep(1.2)
    clear()

# Mensagem com input
def messageInput(msg):
    clear()
    rtn = input(msg)
    clear()
    return rtn

# Limpa a tela
def clear():
    os.system( 'cls' )

# menu principal
def menu():
    while True:
        print ('Escolha um a opção:')
        print ('1 - Criar lista vazia')
        print ('2 - Inserir no início de uma lista')
        print ('3 - Inserir no fim de uma lista')
        print ('4 - Limpar lista')
        print ('5 - Exibir dados do primeiro elemento')
        print ('6 - Exibir dados do último elemento')
        print ('7 - Exibir todos os valores da lista')
        print ('8 - Exibir o tamanho da lista')
        print ('9 - Eliminar primeiro elemento')
        print ('10 - Eliminar último elemento')
        print ('11 - Eliminar elemento buscado')
        print ('12 - Buscar Dados')
        print ('13 - Sair')
        print ('')
        option = int(input('Digite: '))

        # Verifica se opção escolhida é valida
        if(option >= 1 and option <= 13):

            # 1 - Criar lista vazia
            if(option==1):
                if('lista' not in locals()):
                    lista=[]
                    message('Lista criada com sucesso!')

                else:
                    while True:
                        rtnOp1 = messageInput('Existe uma lista criada. Deseja apaga-lá e criar uma nova?(S/N):')
                        if (rtnOp1.lower() == 's'):
                            lista=[]
                            break
                        elif (rtnOp1.lower() =='n'):
                            break
                        else:
                            message('Informe um valor válido')


            # 2 - Inserir no início de uma lista
            elif (option==2):
                if('lista' in locals()):
                    rtn = messageInput('Digite um valor: ')
                    lista.insert(0, rtn)
                    if (rtn in lista):
                        message('Valor inserido com sucesso!')
                else:
                    message('Crie uma lista antes de continuar')


            # 3 - Inserir no fim de uma lista
            elif (option==3):
                if('lista' in locals()):
                    rtn = messageInput('Digite um valor: ')
                    lista.append(rtn)
                    if (rtn in lista):
                        message('Valor inserido com sucesso!')
                else:
                    message('Crie uma lista antes de continuar')


            # 4 - Limpar lista
            elif (option==4):
                if('lista' in locals()):
                    while True:
                        rtnOp1 = messageInput('Deseja limpar a lista?(S/N):')
                    if (rtnOp1.lower() == 's'):
                        lista=[]
                        break
                    elif (rtnOp1.lower() =='n'):
                        break
                    else:
                        message('Informe um valor válido')
                else:
                    message('Crie uma lista antes de continuar')


            # 5 - Exibir dados do primeiro elemento
            elif (option==5):
                if('lista' in locals()):
                    message('Primeiro elemento: '+ lista[0])
                else:
                    message('Crie uma lista antes de continuar')


            # 6 - Exibir dados do último elemento
            elif (option==6):
                if('lista' in locals()):
                    message('Primeiro elemento: '+ lista[len(lista)-1])
                else:
                    message('Crie uma lista antes de continuar')


            # 7 - Exibir todos os valores da lista
            elif (option==7):
                if('lista' in locals()):
                    message('Valores da lista: '+ str(lista))
                else:
                    message('Crie uma lista antes de continuar')


            # 8 - Exibir o tamanho da lista
            elif (option==8):
                if('lista' in locals()):
                    message('Total de: '+ str(len(lista)) + ' registro(s)')
                else:
                    message('Crie uma lista antes de continuar')


            # 9 - Eliminar primeiro elemento
            elif (option==9):
                if('lista' in locals()):
                    lista.pop(0)
                    message('Primeiro valor removido com sucesso!')
                else:
                    message('Crie uma lista antes de continuar')


            # 10 - Eliminar último elemento
            elif (option==10):
                if('lista' in locals()):
                    lista.pop()
                    message('Primeiro valor removido com sucesso!')
                else:
                    message('Crie uma lista antes de continuar')


            # 11 - Eliminar elemento buscado
            elif (option==11):
                if('lista' in locals()):
                    rtn = messageInput('Digite um valor:')
                    ctn = lista.count(rtn)
                    if ctn > 0:
                        lista.remove(rtn)
                        message('Valor removido com sucesso!')
                    else:
                        message('Valor não encontrado.')
                else:
                    message('Crie uma lista antes de continuar')


            # 12 - Buscar Dados
            elif (option==12):
                if('lista' in locals()):
                    rtn = messageInput('Digite um valor:')
                    ctn = lista.count(rtn)
                    if ctn > 0:
                        message('O valor ' + str(rtn) + ' está na posição ' + str(lista.index(rtn)) + ' da lista')
                    else:
                        message('Valor não encontrado.')
                else:
                    message('Crie uma lista antes de continuar')


            # 13 - Sair
            elif (option==13):
                message('Até mais!')
                break
    clear()

# executa o menu principal
menu()
