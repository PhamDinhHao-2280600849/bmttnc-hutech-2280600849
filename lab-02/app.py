from flask import Flask, render_template, request,json
from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/vigenereCipher")
def playfail():
    return render_template('VigenereCipher.html')


@app.route("/encryptCaesar", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    cipher = CaesarCipher()
    encrypted_text = cipher.encrypt_text(text, key)
    return f"Text: {text}<br/>Key: {key}<br/>Encrypted text: {encrypted_text}"


@app.route("/decryptCaesar", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    cipher = CaesarCipher()
    decrypted_text = cipher.decrypt_text(text, key)
    return f"Text: {text}<br/>Key: {key}<br/>Decrypted text: {decrypted_text}"

@app.route("/encryptVigenereCipher", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    vigenereCipher = VigenereCipher();
    encrypted_text = vigenereCipher.vigenere_encrypt(text,key)
    return f"Text: {text}<br/>Key: {key}<br/>Encrypted text: {encrypted_text}"

@app.route("/decryptVigenereCipher", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    vigenereCipher = VigenereCipher();
    decrypted_text = vigenereCipher.vigenere_decrypt(text,key)
    return f"Text: {text}<br/>Key: {key}<br/>Decrypted text: {decrypted_text}"

if __name__ == "__main__":
    app.run(debug=True)
