import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

# Ruta de la base de datos (debe estar en la raíz del proyecto)
DATABASE = "database/datos.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route("/")
def index():
    conn = get_db_connection()

    # Obtener datos del restaurante
    restaurante = conn.execute(
        "SELECT * FROM restaurante LIMIT 1"
    ).fetchone()

    # Obtener menú del almuerzo por fecha específica
    menu = conn.execute(
        "SELECT * FROM menu_almuerzo WHERE fecha = '2026-03-22'"
    ).fetchall()

    conn.close()

    return render_template(
        "index.html",
        restaurante=restaurante,
        menu=menu
    )


if __name__ == '__main__':
    ##app.run(debug=True)
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)