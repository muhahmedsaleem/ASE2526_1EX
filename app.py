from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/lower')
def to_lower():
    s = request.args.get('s')
    if s is None:
        return jsonify({"error": "Missing parameter 's'"}), 400
    return jsonify({"result": s.lower()}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)