import requests
import sympy
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def homepage():
  return 'Processo 2 - Calculo dos números primos'

@app.route('/numprimos/<cod_inicial>/<n>')
def numprimos(cod_inicial,n):

  print ('Solicitação recebida')
  cod_inicial = int(cod_inicial)  
  n = int(n)  
  
  if (cod_inicial >= 1000000 and n >= 5000 and n <= 15000):
  
    # calculando os primos a esquerda do numero
    i = cod_inicial
    vet = []
    qtdvetor = 0

    while (qtdvetor < n):
      i = i-1
      if sympy.isprime(i):
        vet.append(i)
      
      qtdvetor = len(vet)
    
    primoleft = qtdvetor - 1

    # calculando os primos a direita do numero
    i = cod_inicial
    vetdir = []
    qtdvetordir = 0
                
    while (qtdvetordir < n):
      i = i+1
      if sympy.isprime(i):
        vetdir.append(i)

      qtdvetordir = len(vetdir)

    primodir = qtdvetordir - 1

    # encontrado os numeros primos, envio a requisicao para o processo 3 calcular a chave
    link = f"https://api-4.kaiquearaujo.repl.co/gerachave/{vet[primoleft]}/{vetdir[primodir]}"
    requisicao = requests.get(link)
    
    #Imprimindo as resposta e retornando para o processo 1
    print ('\nNúmeros encontrados no processo 2: ')
    print (requisicao.json()['Primo left'] + ' <------ ' + str(cod_inicial) + ' ------> ' + requisicao.json()['Primo dir'])

    print ('\nChave gerada pelo processo 3: ')
    print (requisicao.json()['Chave'])
    
    return requisicao.json()

  else:
    resposta = {"Chave": 'Parâmetros inválidos'}
    return jsonify(resposta)
    
app.run(host='0.0.0.0')
