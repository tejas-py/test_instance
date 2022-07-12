from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# define the CORS
CORS(app)
cors = CORS(app, resources={
    r"/*": {
        "origin": "*"
    }
})


# list the assets in the wallet
@app.route('/')
def home_page():
    return "<b>WELCOME TO THE HOME PAGE</b>"


# running the API
if __name__ == "__main__":
    app.run(debug=True, port=2000)
