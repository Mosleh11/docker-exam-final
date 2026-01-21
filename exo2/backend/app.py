import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Chemin vers la base de données dans le volume partagé
DB_PATH = '/data/users.db'

# Initialisation de la BDD au démarrage
def init_db():
    # On se connecte au fichier SQLite
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # On crée la table si elle n'existe pas (username + password requis)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# On lance l'init au démarrage de l'app
if not os.path.exists('/data'):
    os.makedirs('/data')
init_db()

# --- ROUTES API (CRUD) ---

# 1. Lecture (READ) [cite: 44]
@app.route('/users', methods=['GET'])
def get_users():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    conn.close()
    # On transforme les données en JSON pour le frontend
    users = [{'id': r[0], 'username': r[1], 'password': r[2]} for r in rows]
    return jsonify(users)

# 2. Création (CREATE) [cite: 43]
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)',
                   (data['username'], data['password']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Utilisateur créé"}), 201

# 3. Suppression (DELETE) [cite: 46]
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Utilisateur supprimé"})

# 4. Mise à jour (UPDATE) [cite: 45]
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET username = ?, password = ? WHERE id = ?',
                   (data['username'], data['password'], user_id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Utilisateur mis à jour"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)