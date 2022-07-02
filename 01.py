from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('index.html')
    if request.method == "POST":
        message = request.form["message"]
        return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
