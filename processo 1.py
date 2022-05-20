import requests
import time
import random

# recebendo os parametros
cod_inicial = input("\nDigite o código inicial: ")
n = input("Digite o valor de n: ")

# enviando a requisicao para o processo 2
inicio = time.time()
link = f"https://api-3.kaiquearaujo.repl.co/numprimos/{cod_inicial}/{n}"
requisicao = requests.get(link)
fim = time.time()
tempo = (fim-inicio)

if (requisicao.json()['Chave'] != 'Parametros invalidos'):
    print('\nRespostas dos processos:')
    print ('\nNúmeros encontrados no processo 2: ')
    print (requisicao.json()['Primo left'] + ' <------ ' + str(cod_inicial) + ' ------> ' + requisicao.json()['Primo dir'])
    print ('\nChave gerada pelo processo 3: ')
    print (requisicao.json()['Chave'])
    print('\nTempo de execução total: %f'%(tempo))   
    
    
    # Aqui inicio a execução de chaves aleatórias
    print('\n----------------------------------------------------------')
    print('Objetivo 2: Geração do máximo de chaves em 5 segundos')
    print('\nChaves Geradas: ')
    tempo = 0
    inicio = time.time()
    cont = 0
    
    while (tempo < 5.0):
        cod_inicial = random.randint(10000001,20000000)
        n = random.randint(5000,15000)
        link = f"https://api-3.kaiquearaujo.repl.co/numprimos/{cod_inicial}/{n}"
        requisicao = requests.get(link)
        fim = time.time()    
        tempo = fim - inicio
        cont += 1
        print (requisicao.json()['Chave'])
        
    print ('\nTotal de chaves geradas em 5 segundos: ', cont)
    print('----------------------------------------------------------')
    
else:
    print('O código inicial precisa ser >= 1000000 e (5.000 <= n <= 15000)')
