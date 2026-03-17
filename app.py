from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# 🔹 Función para conectar a la base de datos
def obtener_recomendaciones(categoria):
    conexion = sqlite3.connect("tienda.db")
    cursor = conexion.cursor()

    cursor.execute("SELECT nombre FROM productos WHERE categoria=?", (categoria,))
    resultados = cursor.fetchall()

    conexion.close()

    # Convertir resultados a lista
    recomendaciones = [r[0] for r in resultados]

    return recomendaciones

# 🔹 Ruta API
@app.route("/recomendar", methods=["POST"])
def recomendar():
    data = request.json

    # lo que envía Botpress
    categoria = data.get("producto", "").lower()

    recomendaciones = obtener_recomendaciones(categoria)

    # Si no hay resultados
    if not recomendaciones:
        recomendaciones = ["No se encontraron productos para esta categoría"]

    return jsonify({
        "recomendaciones": recomendaciones
    })

# 🔹 Ejecutar servidor
if __name__ == "__main__":
    app.run(port=5000)