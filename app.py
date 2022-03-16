from asyncio import tasks
from django.http import QueryDict
from flask import Flask, render_template, request
from src.QueryProcessor import QueryProcessor
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    return render_template('index.html')

@app.route("/results", methods=["POST", "GET"])
def results():
    if request.method == 'POST':
        query = request.form['query']

        q = QueryProcessor()
        result_set = q.ProcessQuery(query)
        return render_template("result.html",tasks = result_set)
        
    else:
        return render_template("result.html")

@app.route("/showDoc/<id>", methods=["POST", "GET"])
def showDoc(id):
    return render_template(id + ".txt")


if __name__ == "__main__":
    app.run(debug=True)
