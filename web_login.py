from flask import Flask, request
import sqlite3
import bcrypt

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user = request.form['user']
        password = request.form['password'].encode('utf-8')
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())

        con = sqlite3.connect("usuarios.db")
        con.execute("INSERT INTO usuarios (nombre, clave) VALUES (?, ?)", (user, hashed))
        con.commit()
        con.close()

        return f"Usuario {user} registrado correctamente con clave cifrada."
    return '''
    <h2>Registro de Usuarios</h2>
    <form method="post">
        Usuario: <input name="user"><br>
        Clave: <input type="password" name="password"><br>
        <input type="submit" value="Registrar">
    </form>
    '''

if __name__ == "__main__":  
    con = sqlite3.connect("usuarios.db")
    con.execute("CREATE TABLE IF NOT EXISTS usuarios (nombre TEXT, clave TEXT)")
    con.close()
    app.run(host="0.0.0.0", port=5800)
