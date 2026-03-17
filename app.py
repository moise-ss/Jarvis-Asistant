from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# 🔹 Crear base de datos automáticamente
def inicializar_db():
    conexion = sqlite3.connect("tienda.db")
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        categoria TEXT
    )
    """)

    productos = [
        # Audífonos
        ("Audifonos Bluetooth", "audifonos"),
        ("Audifonos Gamer RGB", "audifonos"),
        ("Audifonos Sony", "audifonos"),
        ("Audifonos Inalambricos Xiaomi", "audifonos"),

        # Computador
        ("Mouse Gamer", "computador"),
        ("Teclado Mecanico RGB", "computador"),
        ("Monitor 24 pulgadas", "computador"),
        ("Base Refrigerante Laptop", "computador"),

        # Celulares
        ("Cargador Rapido", "celular"),
        ("Funda para Celular", "celular"),
        ("Protector de Pantalla", "celular"),
        ("Power Bank 10000mAh", "celular"),

        # Gaming
        ("Control PS5", "gaming"),
        ("Silla Gamer", "gaming"),
        ("Mousepad Gamer XL", "gaming"),

        # Audio
        ("Parlante Bluetooth", "audio"),
        ("Barra de Sonido", "audio"),
        ("Subwoofer", "audio")
    ]

    cursor.executemany("INSERT INTO productos (nombre, categoria) VALUES (?, ?)", productos)

    conexion.commit()
    conexion.close()

# 🔹 Detectar categoría
def detectar_categoria(texto):
    texto = texto.lower()

    if "audifono" in texto or "escuchar" in texto:
        return "audifonos"
    elif "jugar" in texto or "gaming" in texto:
        return "gaming"
    elif "celular" in texto or "telefono" in texto:
        return "celular"
    elif "computador" in texto or "pc" in texto:
        return "computador"
    elif "musica" in texto or "sonido" in texto:
        return "audio"
    else:
        return texto  # usa lo que escribió directamente

def obtener_recomendaciones(categoria):
    conexion = sqlite3.connect("tienda.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre FROM productos WHERE categoria=?", (categoria,))
    resultados = cursor.fetchall()
    conexion.close()
    return [r[0] for r in resultados]
@app.route("/recomendar", methods=["POST"])
def recomendar():
    data = request.json
    texto_usuario = data.get("producto", "")

    categoria = detectar_categoria(texto_usuario)
    recomendaciones = obtener_recomendaciones(categoria)
    if not recomendaciones:
        recomendaciones = ["No se encontraron productos para esta búsqueda"]
    return jsonify({
        "categoria_detectada": categoria,
        "recomendaciones": recomendaciones
    })
if __name__ == "__main__":
    inicializar_db() 
    app.run(port=5000)