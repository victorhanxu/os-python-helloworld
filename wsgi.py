from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello! This is my Openshift App!"

if __name__ == "__main__":
    application.run()
