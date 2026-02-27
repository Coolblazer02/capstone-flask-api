from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta GET /info
@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "aplicacion": "API Capstone",
        "version": "1.0",
        "author": "Victor",
        "descripcion": "API basica usando Flask para demostrar arquitectura Cliente/Servidor"
    })

# Ruta POST /mensaje
@app.route("/mensaje", methods=["POST"])
def mensaje():
    data = request.json

    if not data or "mensaje" not in data:
        return jsonify({"error": "Debes enviar un mensaje en formato JSON"}), 400
    
    texto = data["mensaje"]

    return jsonify({
        "respuesta": f"servidor recibio tu mensaje: '{texto}' correctamente."
    }), 200 

if __name__ == "__main__":
    app.run(debug=True)