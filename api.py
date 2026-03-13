from flask import Flask, request, jsonify

app = Flask(__name__)
from flask_cors import CORS
CORS(app)

@app.route("/calcular", methods=["POST"])
def calcular():
    dados = request.get_json()

    num1 = dados.get("num1")
    num2 = dados.get("num2")
    operacao = dados.get("operacao")

    if operacao == "soma":
        resultado = num1 + num2
    elif operacao == "subtracao":
        resultado = num1 - num2
    elif operacao == "multiplicacao":
        resultado = num1 * num2
    elif operacao == "divisao":
        if num2 == 0:
            return jsonify({"erro": "Divisão por zero"}), 400
        resultado = num1 / num2
    else:
        return jsonify({"erro": "Operação inválida"}), 400

    return jsonify({
        "num1": num1,
        "num2": num2,
        "operacao": operacao,
        "resultado": resultado
    })

if __name__ == "__main__":
    app.run(debug=True)