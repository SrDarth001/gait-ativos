from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

def conectar_banco():
    return mysql.connector.connect(
        host="db-gait",
        user="root",
        password="root",
        database="gait"
    )

@app.route('/ativos', methods=['POST'])
def cadastrar_ativo():
    dados = request.json
    equipamento = dados.get('equipamento')
    horas_uso = int(dados.get('horas_uso'))

    if horas_uso < 25000:
        destino = "Reaproveitar (Realocar)"
    else:
        destino = "Sanitizar e Descartar"

    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO ativos (equipamento, horas_uso, destino_recomendado) VALUES (%s, %s, %s)",
        (equipamento, horas_uso, destino)
    )
    conexao.commit()
    cursor.close()
    conexao.close()

    return jsonify({"mensagem": f"Ativo registrado! Recomendação: {destino}"}), 201

@app.route('/ativos', methods=['GET'])
def listar_ativos():
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ativos")
    resultados = cursor.fetchall()
    cursor.close()
    conexao.close()

    return jsonify(resultados)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
