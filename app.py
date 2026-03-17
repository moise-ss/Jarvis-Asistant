from flask import Flask, jsonify

app = Flask(__name__)
productos = [
    {"id": 1, "nombre": "Audífonos Bluetooth Sony", "precio": 250, "categoria": "audio"},
    {"id": 2, "nombre": "Audífonos Gamer RGB", "precio": 180, "categoria": "audio"},
    {"id": 3, "nombre": "Mouse Gamer Logitech", "precio": 120, "categoria": "gaming"},
    {"id": 4, "nombre": "Teclado Mecánico RGB", "precio": 200, "categoria": "gaming"},
    {"id": 5, "nombre": "Laptop HP i5", "precio": 2800, "categoria": "computo"},
    {"id": 6, "nombre": "Monitor 24 pulgadas", "precio": 900, "categoria": "computo"},
    {"id": 7, "nombre": "Celular Samsung Galaxy", "precio": 2200, "categoria": "movil"},
    {"id": 8, "nombre": "iPhone 13", "precio": 3500, "categoria": "movil"},
    {"id": 9, "nombre": "Tablet Lenovo", "precio": 1300, "categoria": "computo"},
    {"id": 10, "nombre": "Parlante Bluetooth JBL", "precio": 300, "categoria": "audio"}
]

#Ruta principal
@app.route("/")
def inicio():
    return "Servidor de tecnología activo "

#Todos los productos
@app.route("/productos", methods=["GET"])
def obtener_productos():
    return jsonify(productos)

#Filtrar por categoría
@app.route("/productos/<categoria>", methods=["GET"])
def productos_por_categoria(categoria):
    filtrados = [p for p in productos if p["categoria"].lower() == categoria.lower()]
    
    if filtrados:
        return jsonify(filtrados)
    else:
        return jsonify({"mensaje": "No hay productos en esta categoría"})
if __name__ == "__main__":
    app.run(debug=True)