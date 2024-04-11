from flask import Flask, render_template, request,json
from cipher.caesar.caesar_cipher import CaesarCipher

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/caesar")
def caesar():
    return render_template('caesar.html')


@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    cipher = CaesarCipher()
    encrypted_text = cipher.encrypt_text(text, key)
    return f"Text: {text}<br/>Key: {key}<br/>Encrypted text: {encrypted_text}"


@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    cipher = CaesarCipher()
    decrypted_text = cipher.decrypt_text(text, key)
    return f"Text: {text}<br/>Key: {key}<br/>Decrypted text: {decrypted_text}"

if __name__ == "__main__":
    app.run(debug=True)
