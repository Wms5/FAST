from flask import Flask, render_template, redirect

app = Flask(__name__,template_folder="templates")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about():
    return  'FAST is a tool....'

if __name__ == '__main__':
    app.run(debug=True)