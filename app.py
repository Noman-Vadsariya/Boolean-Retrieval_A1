from flask import Flask, render_template, request
from src.QueryProcessor import QueryProcessor
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():

    if request.method == 'POST':
        query = request.form['query']

        if query != "":

            q = QueryProcessor()
            result_set = q.ProcessQuery(query)
            return render_template("result.html",tasks = result_set)
            
        else:
            return render_template("index.html")
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
