from flask import Flask, jsonify, request

# Adicionando um comentário intencionalmente errado para simular o gatilho do pipeline 

app = Flask(__name__)

def calculate_shipping(base_price, tax_rate):
    """
    Calcula o frete total.
    BUG INTENCIONAL: tax_rate virá como string e causará TypeError
    ao somar com base_price (float).
    """
    # O erro está aqui: falta converter tax_rate para float
    return base_price + tax_rate

@app.route('/shipping', methods=['POST'])
def shipping():
    data = request.json
    try:
        price = data.get('price')
        # Simulando um dado vindo de configuração externa como string
        tax = "5.50" 
        
        total = calculate_shipping(price, tax)
        return jsonify({"total": total}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)