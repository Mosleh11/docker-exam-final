import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/random-user', methods=['GET'])
def get_random_user():
    try:
        # C'est LA consigne : passer par le proxy Tor (port 9050 du conteneur 'tor')
        proxies = {
            'http': 'socks5h://tor:9050',
            'https': 'socks5h://tor:9050'
        }
        
        # On appelle l'API externe via le tunnel
        # URL imposée par le sujet
        response = requests.get('https://randomuser.me/api/', proxies=proxies, timeout=10)
        data = response.json()
        
        # On extrait juste ce qu'il faut pour le frontend
        user = data['results'][0]
        return jsonify({
            'name': f"{user['name']['first']} {user['name']['last']}",
            'picture': user['picture']['large']
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)