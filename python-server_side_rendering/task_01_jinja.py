from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

@app.route('/')
def home():
    data = {
        "title": "My Flask App",
        "heading": "Welcome to My Flask App",
        "paragraph": "This is a simple Flask application.",
        "items": ["Flask", "HTML", "Templates"]
    }
    return render_template('index.html', **data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
