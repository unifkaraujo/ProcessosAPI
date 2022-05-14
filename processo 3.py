from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def homepage():
  return 'Processo 3 - Cálculo da chave'

@app.route('/gerachave/<num1>/<num2>')
def gerachave(num1,num2):

  print ('Solicitação recebida')
  
  # gerando a chave
  resultado = int(num1)*int(num2)
  
  print ('\nChave gerada: ',resultado)
  resposta = {"Chave": resultado,"Primo left": num1, "Primo dir": num2}
  return jsonify(resposta)
  
app.run(host='0.0.0.0')