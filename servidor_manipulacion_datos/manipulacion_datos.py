from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista en memoria para guardar usuarios
usuarios = []

# GET /info
@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "sistema": "Servidor Flask de prueba",
        "version": "1.0",
        "autor": "Victor"
    })

# POST /crear_usuario
@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    data = request.json

    # Validación
    if not data:
        return jsonify({"error": "No se enviaron datos"}), 400

    nombre = data.get("nombre")
    correo = data.get("correo")

    if not nombre or not correo:
        return jsonify({"error": "Faltan nombre o correo"}), 400

    usuario = {
        "nombre": nombre,
        "correo": correo
    }

    usuarios.append(usuario)

    return jsonify({"mensaje": "Usuario creado", "usuario": usuario})

# GET /usuarios
@app.route("/usuarios", methods=["GET"])
def obtener_usuarios():
    return jsonify({"usuarios": usuarios})

if __name__ == "__main__":
    app.run(debug=True)