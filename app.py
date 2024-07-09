from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Update the route to handle the `M` and `F` values for gender
@app.route('/search', methods=['GET'])
def search():
    documento_id = 107  # This value is fixed as per your requirements
    sexo = request.args.get('sexo')
    nro_documento = request.args.get('nro_documento')

    if not sexo or not nro_documento:
        return jsonify({'error': 'Missing parameters'}), 400

    # Translate `M` and `F` to the respective `sexo_id` values
    sexo_id = 110 if sexo == 'M' else 111 if sexo == 'F' else None

    if not sexo_id:
        return jsonify({'error': 'Invalid sexo value, must be M or F'}), 400

    url = f"https://teleconsulta.msal.gov.ar/api/pacientes/exists?documento_id={documento_id}&sexo_id={sexo_id}&nro_documento={nro_documento}"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json'
    }
    auth = ('benitezser@gmail.com', 'Dante2303')

    response = requests.get(url, headers=headers, auth=auth)
    
    if response.status_code != 200:
        return jsonify({'error': 'Failed to retrieve data'}), response.status_code

    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

