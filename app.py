from flask import Flask, render_template, request

app = Flask(__name__)

def encrypt_char(char, key):
    if char.islower():
        return chr((ord(char) - ord('a') + key) % 26 + ord('a'))
    elif char.isupper():
        return chr((ord(char) - ord('A') + key) % 26 + ord('A'))
    else:
        return char

def encrypt_caesar(text, key):
    encrypted_text = ''.join(encrypt_char(char, key) for char in text)
    return encrypted_text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        key = int(request.form['key'])
        encrypted_text = encrypt_caesar(text, key)
        return render_template('index.html', encrypted_text=encrypted_text, text=text, key=key)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
