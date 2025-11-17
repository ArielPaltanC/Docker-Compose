from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def init_db():
    db = mysql.connector.connect(
        host="db",
        user="root",
        password="1234",
        database="usuarios_db"
    )
    cursor = db.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100)
        )
    """)
    cursor.execute("SELECT COUNT(*) FROM usuarios")
    if cursor.fetchone()[0] == 0:
        cursor.executemany("INSERT INTO usuarios (nombre) VALUES (%s)", [
            ("Juan",), ("Ana",), ("Carlos",)
        ])
    db.commit()
    db.close()

@app.route('/')
def home():
    return jsonify({"message": "Microservicio de usuarios activo"})

@app.route('/usuarios')
def get_usuarios():
    db = mysql.connector.connect(
        host="db",
        user="root",
        password="1234",
        database="usuarios_db"
    )
    cursor = db.cursor()
    cursor.execute("SELECT nombre FROM usuarios")
    result = [row[0] for row in cursor.fetchall()]
    db.close()
    return jsonify(result)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)

