from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient
import db # Database operations
import os


app = Flask(__name__)
api = Api(app)

db_client = db.Mongodb(os.environ['MONGODB_HOSTNAME'])
db_client.connect()
db_client.set_db("brevetsdb")
db_client.set_collection("latestsubmit")

###
# Resources
###
def csv_form(rows):
    headers = list(rows[0].keys())
    result = ",".join(headers) + "\n"
    for row in rows:
        row_value = list(row.values())
        result += ",".join(row_value) + "\n"
    return result

class listAll(Resource):
    def get(self, dtype):
        args = request.args.get("top", default=-1)
        # Retrieve all the rows with the specific fields in the collection
        rows = db_client.find_fields(["km", "open", "close"])
        # Check if the collection is empty
        if len(rows) == 0:
            return "The database is empty. Please, submit the control time."
        # Check the data type
        if dtype == 'csv':
            result = csv_form(rows)
        elif dtype == 'json':
            result = rows
        else:
            result = "The data can be listed in either csv format or json format! Try 'csv' or 'json'."
        return result


class listOpenOnly(Resource):
    def get(self, dtype):
        args = request.args.get("top", default=-1)
        # Retrieve all the rows with the specific fields in the collection
        rows = db_client.find_fields(["km", "open"])
        # Check if the collection is empty
        if len(rows) == 0:
            return "The database is empty. Please, submit the control time."
        # Check the data type
        if dtype == 'csv':
            result = csv_form(rows)
        elif dtype == 'json':
            result = rows
        else:
            result = "The data can be listed in either csv format or json format! Try 'csv' or 'json'."
        return result


class listCloseOnly(Resource):
    def get(self, dtype):
        args = request.args.get("top", default=-1)
        # Retrieve all the rows with the specific fields in the collection
        rows = db_client.find_fields(["km", "close"])
        # Check if the collection is empty
        if len(rows) == 0:
            return "The database is empty. Please, submit the control time."
        # Check the data type
        if dtype == 'csv':
            result = csv_form(rows)
        elif dtype == 'json':
            result = rows
        else:
            result = "The data can be listed in either csv format or json format! Try 'csv' or 'json'."
        return result

#############

# Create routes
api.add_resource(listAll, '/listAll/<str:dtype>')
api.add_resource(listOpenOnly, '/listOpenOnly/<str:dtype>')
api.add_resource(listCloseOnly, '/listCloseOnly/<str:dtype>')


# Run the application
if __name__ == "__main__":
    app.run(port=CONFIG.PORT, host="0.0.0.0")
