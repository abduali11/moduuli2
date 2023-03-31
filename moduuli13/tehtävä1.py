from flask import Flask, request, jsonify

app = Flask(__name__)

def alkuluku(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

@app.route('/alkuluku/<int:num1>')
def calculate_sum(num1):
    if alkuluku(num1):
        result = {"Numero": num1, "alkuluku": True}
    else:
        result = {"Numero": num1, "alkuluku": False}
    return jsonify(result)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
