from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('Hello_world\templates\hello_world.html', message="hello!")

if __name__ == '__main__':
    app.run(port=8000)