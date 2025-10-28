from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    print("🔹 Rendering index.html...")  # Debug print
    return render_template('index.html')

@app.route('/contact')
def contact():
    print("🔹 Rendering contact.html...")  # Debug print
    return render_template('contact.html')

@app.route('/success')
def success():
    print("🔹 Rendering success.html...")  # Debug print
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)




