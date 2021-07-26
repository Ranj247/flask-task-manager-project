import os
from flask import Flask
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


# Remember the '/' refers to the default route.
@app.route("/")
def hello():
    return "Hello World ... again!"


# To tell our app how and where to run our application
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
