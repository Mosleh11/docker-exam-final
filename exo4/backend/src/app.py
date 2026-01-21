import os
import psycopg2
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Récupération des variables d'environnement (Sécurité !)
DB_NAME = os.environ.get('DB_NAME')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        port=DB_PORT
    )
    return conn

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        # On crée une table simple si elle n'existe pas et on ajoute une donnée
        cur.execute('CREATE TABLE IF NOT EXISTS test (id serial PRIMARY KEY, message varchar(100));')
        cur.execute('INSERT INTO test (message) VALUES (%s)', ('Bonjour depuis PostgreSQL !',))
        conn.commit()
        
        # On lit la donnée
        cur.execute('SELECT message FROM test LIMIT 1;')
        message = cur.fetchone()[0]
        
        cur.close()
        conn.close()
        return jsonify(message=message)
    except Exception as e:
        return jsonify(error=str(e)), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)