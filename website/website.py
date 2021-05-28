from flask import Flask, render_template, request, jsonify
import requests, os


###
# Globals
###

app = Flask(__name__)


###
# Pages
###

@app.route("/")
@app.route("/index")
def home():
    return render_template('index.html')

@app.route("/listAll")
def listall():
    top = request.args.get("top", type=str)
    data_type = request.args.get("datatype", type=str)
    url = 'http://' + os.environ['BACKEND_ADDR'] + ':' + os.environ['BACKEND_PORT'] + '/listAll'
    if data_type == "csv":
        url += '/csv'
    if int(top) > 0:
        url += '?top=' + top
    app.logger.debug(requests.get(url).text)
    r = requests.get(url).text
    return jsonify(result=r)

""""@app.route("/insert", methods=["POST"])
def submit():
    data = request.form.to_dict()
    # Converting string representation of list to a list
    data['table'] = eval(data['table'])
    table = data['table']
    # Remove the previous submit result
    db_client.delete_all_rows()

    for i in range(len(table)):
        row = table[str(i)]
        for key, value in row.items():
            if key == "km":
                row[key] = int(value)
        db_client.insert(row)
    return flask.jsonify(output=str(data))
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
